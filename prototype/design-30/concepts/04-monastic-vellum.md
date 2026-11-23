# Monastic Vellum — *The Sepia Scriptorium*

Parchemin monastique : brun sépia sombre, enluminures, marge rubriquée, encre pâle.

**Palette :** Vellum `#2A1E12` (fond), Encre `#E8D7B0` (texte), Rubrique `#8C2F24` (marge, accent), Or `#B08A4A` (enluminures), Ombre `#16100A` (panneaux).

**Typographie :** Cardo — empattements de copiste, corps 17px/1.7 justifié, titres en unciales espacées.

**Motif custom :** vrille de vigne enluminée SVG — volutes et rubiques aux angles, répétée en filigrane global via `background-image`, jamais par fiche.

**Décisions :**
1. `.gloss` en bandeau de parchemin : `border-left: 4px solid` rubrique, dégradé sépia, marge rubriquée.
2. `.entity` en enluminure : `::first-letter` initiale dorée (`float:left`, `font-size:3em`), filet or au survol.
3. `.brand-mark` remplacé par une vrille SVG, `opacity:.10`, derrière l'en-tête — aucun logo copié.

**Risque :** le brun sépia et l'or des initiales réduisent le contraste ; valider AA sur le corps.
