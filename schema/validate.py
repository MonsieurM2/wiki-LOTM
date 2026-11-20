"""Gate for chapter data. Standard library only; run before any site generation.

Usage: python schema/validate.py <chapter.json>... [--strict]
       python schema/validate.py --self-check
"""

import json
import sys
from pathlib import Path

RELATIONS = {
    "APPEARS_IN": "CONTAINS_MENTION", "PARTICIPATED_IN": "HAS_PARTICIPANT",
    "OCCURS_IN": "CONTAINS_EVENT", "MEMBER_OF": "HAS_MEMBER",
    "LOCATED_IN": "CONTAINS_LOCATION", "OWNS": "OWNED_BY", "USES": "USED_BY",
    "FOLLOWS_PATHWAY": "HAS_FOLLOWER", "HOLDS_SEQUENCE": "HELD_BY",
    "RELATED_TO": "RELATED_TO", "OPPOSES": "OPPOSED_BY", "MENTOR_OF": "MENTORED_BY",
}
REQUIRED = {"id", "book", "number", "title", "text", "status",
            "evidence", "mentions", "events", "relations"}


def check(doc):
    errors = []
    missing = REQUIRED - doc.keys()
    if missing:
        errors.append(f"missing fields: {sorted(missing)}")
        return errors
    if doc["id"] != f'C{doc["number"]:04d}':
        errors.append(f'{doc["id"]}: id/number mismatch')
    evidence = {}
    for ev in doc["evidence"]:
        eid = ev["id"]
        if eid in evidence:
            errors.append(f"duplicate evidence {eid}")
        evidence[eid] = ev
        quote = ev["quote"]
        if quote not in doc["text"]:
            errors.append(f"{eid}: quote is not a substring of chapter text")
        elif ev.get("offsets") and doc["text"][ev["offsets"][0]:ev["offsets"][1]] != quote:
            errors.append(f"{eid}: offsets do not match quote")
        if ev["chapter"] != doc["number"] or ev["book"] != doc["book"]:
            errors.append(f"{eid}: book/chapter mismatch")
    for group in ("mentions", "events", "relations"):
        for item in doc[group]:
            for ref in item["evidence_ids"]:
                if ref not in evidence:
                    errors.append(f'{group}: unresolved evidence {ref}')
    for rel in doc["relations"]:
        kind = rel["type"]
        if kind not in RELATIONS or rel["inverse"] != RELATIONS[kind]:
            errors.append(f"invalid relation/inverse pair: {kind}/{rel['inverse']}")
        if kind == "RELATED_TO" and not rel.get("label"):
            errors.append("RELATED_TO requires a label")
    return errors


def self_check():
    example = Path(__file__).parent / "examples" / "chapter-0001.json"
    doc = json.loads(example.read_text(encoding="utf-8"))
    assert check(doc) == [], check(doc)
    broken = json.loads(json.dumps(doc))
    broken["evidence"][0]["quote"] = "a quote that is not in the text"
    assert any("substring" in e for e in check(broken))
    print("self-check OK")


def main(paths, strict):
    docs = [json.loads(Path(p).read_text(encoding="utf-8")) for p in paths]
    bad = 0
    for path, doc in zip(paths, docs):
        errors = check(doc)
        if errors:
            bad += 1
            for error in errors:
                print(f"{path}: {error}", file=sys.stderr)
    if strict:
        numbers = sorted(d["number"] for d in docs)
        if numbers != list(range(1, 1395)):
            print("strict: expected chapters 1..1394 exactly once", file=sys.stderr)
            bad += 1
    print(f"{len(docs)} chapter(s) checked, {bad} invalid")
    return 1 if bad else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--self-check" in args:
        self_check()
    else:
        sys.exit(main([a for a in args if a != "--strict"], "--strict" in args))
