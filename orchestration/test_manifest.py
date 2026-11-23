"""Self-check for the resumable manifest. Run: python orchestration/test_manifest.py"""

import json
import tempfile
from pathlib import Path

from manifest import BATCH_SIZE, CHAPTERS, Manifest


def check(root):
    m = Manifest(root).init()
    assert len(m.data["chapters"]) == CHAPTERS
    assert m.status()["batches"] == (CHAPTERS + BATCH_SIZE - 1) // BATCH_SIZE
    assert m.status()["pending"] == CHAPTERS

    # Claim two chapters, then simulate a crash: they stay in_progress.
    first, batch = m.next("crashed-agent")
    second, _ = m.next("crashed-agent")
    assert (first, second, batch) == (1, 2, 1)
    assert Manifest(root).load().status()["in_progress"] == 2

    # A fresh process recovers the stale claims; attempts are kept for cost.
    resumed = Manifest(root).load()
    assert resumed.recover() == 2
    assert resumed.status()["pending"] == CHAPTERS
    assert resumed.status()["in_progress"] == 0
    assert resumed.chapter(1)["attempts"] == 1  # recovery is not a new attempt

    # Resume is exactly where execution stopped, and the new claim is counted.
    again, _ = resumed.next("worker")
    assert again == first
    assert resumed.chapter(1)["attempts"] == 2

    # A chapter cannot be marked done without its generated JSON.
    try:
        resumed.complete(again)
        raise AssertionError("complete accepted a missing chapter file")
    except ValueError:
        pass
    resumed.chapters_dir.mkdir(parents=True, exist_ok=True)
    (resumed.chapters_dir / "C0001.json").write_text("{}", encoding="utf-8")
    resumed.complete(again)
    assert resumed.status()["done"] == 1

    next_chapter, _ = resumed.next("worker")
    assert next_chapter == second
    resumed.dispute(next_chapter)
    assert resumed.status()["dispute"] == 1

    # Journal is append-only but a retry must not duplicate an entry.
    assert resumed.record(2, "EV-0002-001", "CORRECT", "x", "y", "anchor", "verifier") is True
    assert resumed.record(2, "EV-0002-001", "CORRECT", "x", "y", "anchor", "verifier") is False
    lines = resumed.journal_path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0])["kind"] == "CORRECT"

    # The manifest on disk is always complete JSON, never half-written.
    json.loads(resumed.path.read_text(encoding="utf-8"))
    assert resumed.status()["estimated_agent_minutes"] > 0
    print("OK: init, claim, crash, recover, resume, complete, dispute, journal dedup")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        check(Path(d))
