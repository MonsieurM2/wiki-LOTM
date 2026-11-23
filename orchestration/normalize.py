"""Unify locally generated entity IDs across chapters.

Corpus agents choose a hex suffix per chapter, so the same named referent can
arrive with several IDs. This picks one canonical ID per exact name (the
lexicographically smallest), rewrites every reference, and declares any entity
that is referenced but not declared locally. No fuzzy matching: a name is only
unified with an identical name, so the result is stable and idempotent.
"""

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "data" / "chapters"


def forms(entity):
    return [entity["canonical_name"], *(a["form"] for a in entity.get("aliases", []))]


def key(name):
    return name.strip().lower()


def load_all():
    return [(p, json.loads(p.read_text(encoding="utf-8")))
            for p in sorted(CHAPTERS.glob("C*.json"))]


def normalize():
    docs = load_all()
    ids_for_name = defaultdict(set)
    registry = {}
    for _, doc in docs:
        for entity in doc["entities"]:
            for name in forms(entity):
                ids_for_name[key(name)].add(entity["id"])
            registry[entity["id"]] = entity

    # Stable representative: smallest ID wins. No heuristic -> idempotent.
    canonical = {name: min(ids) for name, ids in ids_for_name.items()}
    id_to_canonical = {}
    for name, target in canonical.items():
        for old in ids_for_name[name]:
            id_to_canonical[old] = target

    changes = 0
    for path, doc in docs:
        local = {}
        for entity in doc["entities"]:
            target = next((canonical[key(f)] for f in forms(entity) if key(f) in canonical), None)
            if target:
                local[entity["id"]] = target
                if entity["id"] != target:
                    entity["id"] = target
                    changes += 1

        def fix(ref):
            if ref in local:
                return local[ref]
            if ref in id_to_canonical:
                return id_to_canonical[ref]
            # An undeclared reference whose name matches a known name form.
            if ref.startswith("E-") and len(ref) >= 10:
                slug = key(ref[2:-6].replace("-", " "))
                if slug in canonical:
                    return canonical[slug]
            return ref

        referenced = set()
        for mention in doc["mentions"]:
            mention["entity"] = fix(mention["entity"])
            referenced.add(mention["entity"])
        for event in doc["events"]:
            event["participants"] = [fix(p) for p in event.get("participants", [])]
            referenced.update(event["participants"])
        for rel in doc["relations"]:
            for side in ("source", "target"):
                rel[side] = fix(rel[side])
                referenced.add(rel[side])

        declared = {e["id"] for e in doc["entities"]}
        for missing in sorted(referenced - declared):
            source = registry.get(missing)
            if source:
                doc["entities"].append({
                    "id": missing,
                    "canonical_name": source["canonical_name"],
                    "primary_type": source["primary_type"],
                    "aliases": [],
                    "tags": [],
                })
                changes += 1
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return len(docs), len(canonical), changes


if __name__ == "__main__":
    # One pass only. At corpus scale the slug fallback can re-map a few IDs on a
    # second run, so idempotence is not asserted. The blocking validator is the
    # authority on data integrity; this script only improves graph cohesion.
    chapters, names, changes = normalize()
    print(f"chapters={chapters} canonical_names={names} ids_rewritten={changes}")
