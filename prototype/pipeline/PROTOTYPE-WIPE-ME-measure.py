"""Prototype-only: compare one extractor output with one verifier output."""

import json
import sys
from collections import Counter
from pathlib import Path

out = Path(__file__).parent / "out"


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def measure(chapter):
    ext = load(out / f"extractor-chapter-{chapter:04d}.json")
    ver = load(out / f"verifier-chapter-{chapter:04d}.json")
    verdicts = {v["evidence_id"]: v for v in ver["verdicts"]}
    counts = Counter(v["verdict"] for v in ver["verdicts"])
    evidence_ids = [e["id"] for e in ext["evidence"]]
    unresolved = [eid for eid in evidence_ids if eid not in verdicts]
    return {
        "chapter": chapter,
        "title": ext["title"],
        "evidence": len(evidence_ids),
        "entities": len({m["entity"] for m in ext["mentions"]}),
        "events": len(ext["events"]),
        "relations": len(ext["relations"]),
        "confirm": counts["CONFIRM"],
        "dispute": counts["DISPUTE"],
        "correct": counts["CORRECT"],
        "unresolved": len(unresolved),
        "disagreement_rate": round((counts["DISPUTE"] + counts["CORRECT"]) / max(len(evidence_ids), 1), 3),
        "causes": [v.get("note", "") for v in ver["verdicts"] if v["verdict"] != "CONFIRM"],
    }


if __name__ == "__main__":
    chapters = [int(a) for a in sys.argv[1:]] or [1, 2, 3]
    rows = [measure(c) for c in chapters]
    for r in rows:
        print(f'ch {r["chapter"]:04d} « {r["title"]} »: {r["evidence"]} evidence, '
              f'{r["entities"]} entités, {r["events"]} events, {r["relations"]} relations | '
              f'confirm={r["confirm"]} dispute={r["dispute"]} correct={r["correct"]} '
              f'non-tranché={r["unresolved"]} taux={r["disagreement_rate"]}')
        for cause in r["causes"]:
            print(f'    - {cause}')
    totals = Counter()
    for r in rows:
        for k in ("evidence", "entities", "events", "relations", "confirm", "dispute", "correct", "unresolved"):
            totals[k] += r[k]
    print("TOTAL", dict(totals))
