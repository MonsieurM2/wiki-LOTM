# Eye of the Fog — *The Unblinking Grey*

Un œil unique dans la brume, gris cendré, blanc sale, vide presque total — minimalisme inquiétant.

**Palette :** Suie `#0B0B0A` (fond), Cendre `#9A9A92` (texte), Blanc sale `#DDD8CC` (titres), Voile `#2A2A27` (panneaux), Pupille `#4A4842` (accent).

**Typographie :** Newsreader, corps 16px/1.9 ; titres en petites capitales très espacées, interlignage large.

**Motif custom :** œil solitaire et cernes concentriques SVG, pupille unique, anneaux de brume en dégradé — ornement global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = œil SVG, `radial-gradient` gris diffus, `opacity:.06` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = cartouche Voile, liseré Cendre 1px, `box-shadow` flou, padding généreux.
3. `.entity` : `::before` anneaux en `repeating-radial-gradient` cendré, filet mince sous le titre.

**Risque :** l'œil peut virer au gimmick ; garder l'opacité très basse, valider AA sur corps et liens.
