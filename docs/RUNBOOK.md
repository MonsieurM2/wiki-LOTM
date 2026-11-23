# Runbook — Case Files wiki

## Current state

The site is live at https://monsieurm2.github.io/wiki-LOTM/. Every push to `main` rebuilds it. The corpus is generated chapter by chapter; see `data/manifest.json` for the authoritative state (1394 chapters, 28 batches of 50).

## Local build

```sh
npm install --prefix site
python schema/validate.py data/chapters/C*.json
python orchestration/normalize.py
npm run build --prefix site
```

The build writes `site/dist/` and runs Pagefind on it. To serve locally with the correct base path, expose `site/dist/` as `/wiki-LOTM/`.

## Corpus generation

1. Pick a batch with `python orchestration/manifest.py next --agent <id> --batch <n>`.
2. The chapter source is `data/source/C####.txt` (header `BOOK b | CHAPTER n | title`, then the full text).
3. An extraction agent writes `data/chapters/C####.json` conforming to `schema/chapter.schema.json`. The prompt pattern is in `docs/site-contract.md` and the issue history.
4. **Independently verify** the written file: reopen the source, confirm every `quote` is a literal substring, recompute every `offset`, and check that no obvious fact was missed. Disagreements go to `data/disagreements.jsonl` via `orchestration/manifest.py journal`.
5. `complete <n>` marks the chapter done only if its JSON exists. `recover` resets stale `in_progress` claims after a crash.
6. Run `normalize.py` after each wave: corpus agents choose local entity-ID suffixes, so the same name can arrive under several IDs. The script unifies them and is idempotent.

## Deployment

`.github/workflows/deploy.yml` runs `npm ci`, `astro build`, Pagefind, then the official Pages actions. GitHub Pages must be configured with `build_type: workflow`; if the site is missing, `POST /repos/MonsieurM2/wiki-LOTM/pages` with `{"build_type":"workflow"}` (PUT returns 404 when Pages is not yet enabled).

## Known limits

- The full corpus is ~255 agent-hours of verification at the measured ~11 min/chapter. Parallel agents shorten wall-clock time but not the total.
- Pagefind has no published on-disk index size for ~26,500 pages; measure at the first full build. If indexing fails, split the index rather than regrouping fichés (ADR 0003).
- The spoiler veil is opt-in only: Pagefind indexes raw text, so masking cannot be guaranteed.
