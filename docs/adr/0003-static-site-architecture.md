# Static site architecture on GitHub Pages

The wiki has 1,394 chapters and roughly 26,500 entity fichés, with no human-managed code or commits. We keep the canonical data as committed JSON in `data/` (one file per chapter) and the presentation in `site/`: Astro reads `data/` and generates static HTML, one page per entity. Exactly four React islands hydrate — search, evidence drawer, date-seeded ritual, opt-in spoiler veil — and everything else stays indexable HTML; the chapter graph is static SVG. Pagefind indexes the generated HTML in a separate step between `astro build` and `upload-pages-artifact`. Pushing to `main` runs one workflow using the official GitHub Actions deployment path, with Pages configured to use "GitHub Actions" as its source.

One page per entity is deliberate. The ~1.3 Go figure that motivated regrouping fichés was never measured: it assumed ~50 Ko per page. The frozen case-file prototype is 12,064 bytes, of which 8,095 is CSS; with CSS and JS shared across pages, a page is ~4 Ko, so 26,500 pages are ~100 Mo — below the 1 Go limit for a published Pages site. Regrouping fichés by type with anchors would have broken stable URLs and Pagefind's per-page granularity to solve a phantom constraint.

## Considered and rejected

- **Group fichés by type with anchors**: rejected — solves an unmeasured constraint and costs stable URLs and index granularity.
- **Inject data from outside the repository at build time**: rejected — adds a mechanism to maintain and loses the git audit trail of every verified fact; a push to `main` is the natural rebuild trigger.
- **Astro collections (`src/content/`) as the canonical store**: rejected — mixes facts with presentation; `data/` plus the blocking validator remains the trust boundary.
- **A third-party deploy action or a `gh-pages` branch**: rejected — the official Actions path is documented and adds no dependency.
- **A custom `astro:build:done` Pagefind integration**: rejected — a separate workflow step needs no integration code and follows the documented order.

## Consequences

Build and deploy are separate jobs, so the 10-minute Pages deployment timeout does not cap indexing time. Measure the real artifact size and index build time at the first full generation; revisit this decision only if the artifact approaches 1 Go or indexing becomes impractical — and then split the index rather than regroup fichés. Pagefind runs with English forced, `data-pagefind-body` on content only, navigation and footer excluded, and `max_fragments` available if file-count limits appear.
