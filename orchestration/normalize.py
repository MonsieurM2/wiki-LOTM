"""Unify locally generated entity IDs across chapters.

Corpus agents choose a hex suffix per chapter, so the same named referent can
arrive with several IDs. This picks one canonical ID per name, rewrites every
reference, and declares any entity that is referenced but not declared locally.
It is idempotent: a second run changes nothing.
"""

import json
from collections import Counter, defaultdict
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
    name_counts = defaultdict(Counter)
    registry = {}
    for _, doc in docs:
        for entity in doc["entities"]:
            for name in forms(entity):
                name_counts[key(name)][entity["id"]] += 1
            registry[entity["id"]] = entity

    canonical = {name: counter.most_common(1)[0][0] for name, counter in name_counts.items()}
    id_to_canonical = {}
    for name, target in canonical.items():
        for old in name_counts[name]:
            id_to_canonical[old] = target

    def slug_to_id(ref):
        """Recover a name from an ID whose hex suffix is no longer registered."""
        if not ref.startswith("E-") or len(ref) < 10:
            return ref
        slug = key(ref[2:-6].replace("-", " "))
        if slug in canonical:
            return canonical[slug]
        tokens = set(slug.split())
        best, score = None, 0
        for name, target in canonical.items():
            current = len(tokens & set(name.split()))
            if current > score:
                best, score = target, current
        return best if score >= max(1, len(tokens) - 1) else ref

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
            return slug_to_id(ref)

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
    chapters, names, changes = normalize()
    print(f"chapters={chapters} canonical_names={names} ids_rewritten={changes}")
    second = normalize()
    assert second[2] == 0, f"normalization is not idempotent: {second[2]} changes"
    print("idempotence: OK")
