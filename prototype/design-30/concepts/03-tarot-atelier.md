# Tarot Atelier — *The Deep Indigo*

Jeu de tarot imprimé : indigo profond, lettres letterpress, cadres épais dorés, papier mat.

**Palette :** Indigo `#1B1B3A` (fond), Nuit `#101028` (panneaux), Or `#C6A24B` (cadres), Papier `#EDE4D0` (texte), Pourpre `#5B3A7A` (accent occulte).

**Typographie :** Cormorant Garamond — empattements letterpress, légèrement encrés ; corps 17px/1.7 justifié, titres en petites capitales espacées.

**Motif custom :** coin d'arcane SVG — volutes et petites étoiles dorées aux quatre angles, répété en filigrane global via `background-image`, jamais par fiche.

**Décisions :**
1. `.gloss` en cadre épais doré (`border: 4px double`, `box-shadow` intime) sur papier mat.
2. `.entity` en letterpress : `text-shadow: 0 1px 0` clair, filet or au survol.
3. `.brand-mark` remplacé par une rosette d'arcane SVG, `opacity:.12`, derrière l'en-tête.

**Risque :** l'or sur indigo et le `text-shadow` letterpress réduisent le contraste ; valider AA sur le corps.
