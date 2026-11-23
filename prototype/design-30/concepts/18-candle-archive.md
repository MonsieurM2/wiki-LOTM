# Candle Archive — *The Wax Ledger*

Archives aux bougies : bois sombre, cire fondue, flaques de lumière ambrée sur étagères, ombres profondes.

**Palette :** Noyer `#120C08` (fond), Cire `#E8D9B5` (texte), Ambre `#D98B32` (flaques), Suie `#241A12` (panneaux), Mèche `#6E4A2A` (accent).

**Typographie :** EB Garamond, corps 16px/1.8 ; titres en petites capitales espacées, lettrage gravé.

**Motif custom :** chandelle et étagères SVG, flaque radiale ambre, gouttes de cire en filigrane — ornement global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = chandelle SVG, `radial-gradient` ambre diffus, `opacity:.10` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = flaque de cire : cartouche Suie, liseré Mèche 1px, `box-shadow` ambre flou.
3. `.entity` : `::before` étagères en `repeating-linear-gradient` Noyer/Suie, filet Cire sous le titre.

**Risque :** l'ambre peut saturer les flaques et nuire à la lisibilité ; désaturer, valider AA sur corps et liens.
