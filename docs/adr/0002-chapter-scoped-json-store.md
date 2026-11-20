# Chapter-scoped JSON store, no generic Fact store

Parallel extraction agents must be able to write without colliding, and one Evidence must be stored once yet cited by many fichés. We keep the canonical data as one JSON file per chapter (0001–1394) holding the cleaned text and all Evidence, Mentions, Events and Relations found in that chapter; fichés, indexes and the link graph are generated from those files and never edited by hand. There is no generic subject–predicate–object `Fact` type: the three defined forms (Mention, Event, Relation) carry `evidence_ids` directly.

## Considered and rejected

- **One large JSON file per collection**: rejected — parallel agents would overwrite each other and a single diff would be unreadable.
- **SQLite as the canonical store**: rejected — a binary file cannot be reviewed in git and adds a runtime dependency to a static build.
- **A universal triple store**: rejected — it would duplicate the three domain forms already defined in `GLOSSARY.md` and invite invented predicates.

## Consequences

Thousands of small files are acceptable to git and Astro, but a validator (`schema/validate.py`) must run before every generation: unique IDs, chapters 1–1394, resolvable Evidence and quotes that are exact substrings of the stored text. A failed check blocks publication.
