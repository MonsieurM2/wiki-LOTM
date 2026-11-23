"""Resumable chapter orchestration for the LOTM corpus.

One manifest records the state of chapters 1-1394: pending, in_progress, done
or dispute. Batches of 50 keep the run restartable. A chapter is claimed
atomically; after a crash the stale in_progress is returned to pending by
`recover`, so the next claim is exactly where the run stopped. Disagreements
go to an append-only, deduplicated JSONL journal.

Only one process writes the manifest: the orchestrator claims chapters and
hands them to parallel agents, which return results. Agents never edit it.

Usage: python orchestration/manifest.py [--root DIR] <command>
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

CHAPTERS = 1394
BATCH_SIZE = 50
STATES = ("pending", "in_progress", "done", "dispute")
KINDS = ("CORRECT", "DISPUTE", "MISSING")
MINUTES_PER_CHAPTER = 11  # measured in prototype/pipeline/VERDICT.md


def now():
    return datetime.now(timezone.utc).isoformat()


class Manifest:
    def __init__(self, root):
        self.root = Path(root)
        self.path = self.root / "data" / "manifest.json"
        self.journal_path = self.root / "data" / "disagreements.jsonl"
        self.chapters_dir = self.root / "data" / "chapters"
        self.data = None

    def load(self):
        self.data = json.loads(self.path.read_text(encoding="utf-8"))
        return self

    def save(self):
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(self.data, indent=2, sort_keys=True), encoding="utf-8")
        tmp.replace(self.path)  # atomic: a crash cannot leave a half-written manifest

    def init(self):
        if self.path.exists():
            raise ValueError("manifest already exists; refusing to overwrite")
        self.data = {
            "version": 1,
            "batch_size": BATCH_SIZE,
            "chapters": {
                f"{n:04d}": {
                    "state": "pending",
                    "batch": (n - 1) // BATCH_SIZE + 1,
                    "attempts": 0,
                    "agent": None,
                    "updated_at": None,
                }
                for n in range(1, CHAPTERS + 1)
            },
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.save()
        return self

    def chapter(self, number):
        return self.data["chapters"][f"{number:04d}"]

    def next(self, agent="agent", batch=None):
        for n in range(1, CHAPTERS + 1):
            entry = self.chapter(n)
            if entry["state"] != "pending":
                continue
            if batch is not None and entry["batch"] != batch:
                continue
            entry["state"] = "in_progress"
            entry["agent"] = agent
            entry["attempts"] += 1
            entry["updated_at"] = now()
            self.save()
            return n, entry["batch"]
        raise ValueError("no pending chapter" + (f" in batch {batch}" if batch else ""))

    def complete(self, number):
        entry = self.chapter(number)
        if entry["state"] != "in_progress":
            raise ValueError(f"chapter {number} is {entry['state']}, not in_progress")
        if not (self.chapters_dir / f"C{number:04d}.json").exists():
            raise ValueError(f"chapter {number}: generated JSON missing; refusing to mark done")
        entry["state"] = "done"
        entry["agent"] = None
        entry["updated_at"] = now()
        self.save()

    def dispute(self, number):
        entry = self.chapter(number)
        if entry["state"] != "in_progress":
            raise ValueError(f"chapter {number} is {entry['state']}, not in_progress")
        entry["state"] = "dispute"
        entry["agent"] = None
        entry["updated_at"] = now()
        self.save()

    def recover(self):
        stale = [n for n in range(1, CHAPTERS + 1) if self.chapter(n)["state"] == "in_progress"]
        for n in stale:
            entry = self.chapter(n)
            entry["state"] = "pending"
            entry["agent"] = None
            entry["updated_at"] = now()
        if stale:
            self.save()
        return len(stale)

    def journal_keys(self):
        if not self.journal_path.exists():
            return set()
        keys = set()
        for line in self.journal_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                entry = json.loads(line)
                keys.add((entry["chapter"], entry["fact_id"], entry["kind"]))
        return keys

    def record(self, chapter, fact_id, kind, before="", after="", reason="", verifier=""):
        if kind not in KINDS:
            raise ValueError(f"kind must be one of {KINDS}")
        key = (chapter, fact_id, kind)
        if key in self.journal_keys():
            return False  # a retry after a crash must not duplicate the journal entry
        self.journal_path.parent.mkdir(parents=True, exist_ok=True)
        entry = {
            "chapter": chapter,
            "fact_id": fact_id,
            "kind": kind,
            "before": before,
            "after": after,
            "reason": reason,
            "verifier": verifier,
            "timestamp": now(),
        }
        with self.journal_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, sort_keys=True) + "\n")
        return True

    def status(self):
        counts = {state: 0 for state in STATES}
        batches = {}
        minutes = 0
        for n in range(1, CHAPTERS + 1):
            entry = self.chapter(n)
            counts[entry["state"]] += 1
            minutes += entry["attempts"] * MINUTES_PER_CHAPTER
            b = entry["batch"]
            batches[b] = batches.get(b, 0) + (1 if entry["state"] == "pending" else 0)
        current = min((b for b, count in batches.items() if count), default=None)
        return {
            **counts,
            "batches": (CHAPTERS + BATCH_SIZE - 1) // BATCH_SIZE,
            "current_batch": current,
            "estimated_agent_minutes": minutes,
        }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    nxt = sub.add_parser("next")
    nxt.add_argument("--agent", default="agent")
    nxt.add_argument("--batch", type=int)
    done = sub.add_parser("complete")
    done.add_argument("chapter", type=int)
    dis = sub.add_parser("dispute")
    dis.add_argument("chapter", type=int)
    sub.add_parser("recover")
    sub.add_parser("status")
    rec = sub.add_parser("journal")
    rec.add_argument("chapter", type=int)
    rec.add_argument("fact_id")
    rec.add_argument("kind", choices=KINDS)
    rec.add_argument("--before", default="")
    rec.add_argument("--after", default="")
    rec.add_argument("--reason", default="")
    rec.add_argument("--verifier", default="")
    args = p.parse_args(argv)

    m = Manifest(args.root)
    if args.command == "init":
        m.init()
        print(json.dumps(m.status()))
    else:
        m.load()
        if args.command == "next":
            chapter, batch = m.next(args.agent, args.batch)
            print(json.dumps({"chapter": chapter, "batch": batch}))
        elif args.command == "complete":
            m.complete(args.chapter)
            print(json.dumps({"chapter": args.chapter, "state": "done"}))
        elif args.command == "dispute":
            m.dispute(args.chapter)
            print(json.dumps({"chapter": args.chapter, "state": "dispute"}))
        elif args.command == "recover":
            print(json.dumps({"recovered": m.recover()}))
        elif args.command == "status":
            print(json.dumps(m.status()))
        elif args.command == "journal":
            added = m.record(args.chapter, args.fact_id, args.kind, args.before,
                             args.after, args.reason, args.verifier)
            print(json.dumps({"added": added}))


if __name__ == "__main__":
    main()
