# Extraction brief — one chapter, one verified JSON

You are a corpus agent for the LOTM wiki. Work only on the chapter numbers given in your task prompt. For each assigned number **N**, write exactly one file: `data/chapters/CNNNN.json` (zero-padded to 4 digits). Do not modify any other file.

## Read first

- `data/source/CNNNN.txt` — line 1 is `BOOK b | CHAPTER n | title`, then the full chapter text.
- `schema/chapter.schema.json` — authoritative schema.
- `data/chapters/C0002.json` — worked example of the exact text convention.

## Output contract

For every assigned chapter:

- `id`: `C` + 4 digits; `book` from the source header; `number`: N; `title`: source title without `Chapter N:`.
- `text`: the chapter body only — drop the `BOOK … | CHAPTER … | title` header and any front-matter title lines, join paragraphs with `\n\n`. This must match the convention of `C0002.json` byte-for-byte in style.
- `entities[]`: every named referent — Character, Event, Chapter, Faction, Location, Artifact, Pathway, Concept. Fields: `id`, `canonical_name`, `primary_type`, `aliases`, `tags`.
- `evidence[]`: 12–20 entries. Fields: `id` (`EV-NNNN-xxx`), `book`, `chapter`, `chapter_title`, `quote` (a **literal substring of `text`**), `offsets` `[start,end]` with `text[start:end] === quote`, `verifier`, `status: "confirmed"`.
- `mentions[]`, `events[]`, `relations[]`: every `evidence_ids` value must resolve to a local evidence; every entity reference must be declared locally. Relation `inverse` must be the exact pair from `schema/validate.py`: APPEARS_IN↔CONTAINS_MENTION, PARTICIPATED_IN↔HAS_PARTICIPANT, OCCURS_IN↔CONTAINS_EVENT, MEMBER_OF↔HAS_MEMBER, LOCATED_IN↔CONTAINS_LOCATION, OWNS↔OWNED_BY, USES↔USED_BY, FOLLOWS_PATHWAY↔HAS_FOLLOWER, HOLDS_SEQUENCE↔HELD_BY, RELATED_TO↔RELATED_TO (requires `label`), OPPOSES↔OPPOSED_BY, MENTOR_OF↔MENTORED_BY. Never put a reverse label in `type` — the forward form above is always `type`.
- `status: "verified"` at chapter level.

## Entity IDs

Before writing, grep the existing `data/chapters/*.json` for any name you use. Recurring characters (Zhou Mingrui, Klein Moretti, Audrey Hall, Alger Wilson, Benson, Melissa, Roselle Gustav, Dunn Smith, Old Neil, etc.) **must reuse their existing canonical ID**. New referents get a new conforming ID `E-<slug>-<6 hex>`. Cross-chapter ID harmonisation is done later by `orchestration/normalize.py` — do not attempt it yourself.

## Mandatory verification before you finish

1. For every evidence: assert `quote in text` and `text[start:end] === quote`. Recompute offsets with `text.index(quote)`; never hand-count.
2. Assert every evidence/entity reference resolves locally.
3. Run `python schema/validate.py <all files you wrote>` from the repo root. Iterate until it reports `0 invalid`.
4. Never invent a fact. If a name has no supporting sentence in the chapter, leave it out.

Write JSON with `json.dump(obj, ensure_ascii=False, indent=2)` and a trailing newline. Report only: files written, counts, validator result, and anything you deliberately skipped.
