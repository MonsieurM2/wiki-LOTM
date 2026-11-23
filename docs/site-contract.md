# Site build contract

The site is generated from `data/chapters/C####.json` (one canonical, validated chapter file). Nothing in `site/` holds facts.

## Chapter JSON

`schema/chapter.schema.json` is authoritative. Every displayed fact carries `book`, `chapter` and a `quote` that is an exact substring of `text`. `evidence[].offsets` point at that quote. Entity IDs match `^E-[a-z0-9]+(?:-[a-z0-9]+)*-[a-f0-9]{6}$`; evidence IDs `EV-\d{4}-\d{3}`.

## File ownership

| Path | Owner |
|---|---|
| `site/src/styles/casefiles.css` | design agent |
| `site/src/components/*.tsx` | island agent |
| `.github/workflows/deploy.yml`, `site/astro.config.mjs`, `site/package.json` | build agent |
| `site/src/layouts/*.astro`, `site/src/pages/**`, `site/src/lib/data.ts` | orchestrator |
| `data/chapters/*.json` | corpus agents (one file per agent) |

## Island props

- `SearchIsland` — no props; loads `/pagefind/pagefind.js` at runtime, renders an input and a result list; each result links to `/chapter/<n>/` or `/entity/<id>/`.
- `EvidenceDrawer` — prop `evidence: {id, quote, book, chapter, chapterTitle}[]`; listens for clicks on `[data-evidence-id]`, opens a modal with the literal quote and its `book`/`chapter` source. Never a summary.
- `Ritual` — no props; 22 Major Arcana seeded by UTC `YYYY-MM-DD`, identical for every visitor that day; cards with a list fallback.
- `SpoilerVeil` — no props; opt-in only, stored in `localStorage`, never on by default; reveals `[data-spoiler]`.

## Design language

Port `PROTOTYPE-FINAL.html` from branch `prototype/design-30` exactly: kraft `#3A342B`, ink `#141210`, cachet `#B04338`, manille `#DCCFB0`, ref `#A89A7A`; monospace typewriter, spaced capitals, red file spine, kraft grain, rotating circular sigil watermark, bracketed classification, framed evidence cards with `REF.` labels, dashed rules. No serif, no rounded cards, no generic SaaS styling.

## Build

`npm run build` runs `astro build` then Pagefind on `site/dist/`. GitHub Actions deploys `site/dist/` with the official Pages actions.
