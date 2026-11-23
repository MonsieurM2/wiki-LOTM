# Fog and Gaslight — *The Amber Veil*

Brouillard londonien, ambre de gaz suintant des réverbères, silhouettes victoriennes noyées de bleu-gris.

**Palette :** Fouraille `#0C1116` (fond), Brume `#8C9AA6` (texte), Ambre `#D9A441` (ampoules), Gaz `#F0C877` (halos), Ardoise `#2A3B47` (panneaux).

**Typographie :** Lora, corps 16px/1.7 ; titres en petites capitales espacées, lettrage gazeux.

**Motif custom :** réverbère et volutes de brume SVG, halo radial ambre, silhouette de chapeau haut-de-forme en filigrane — ornement global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = réverbère SVG, `radial-gradient` ambre diffus, `opacity:.12` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = halo de gaz : cartouche Ardoise, liseré Ambre, `box-shadow` flou ambre.
3. `.entity` : `::before` volutes de brume en `linear-gradient` bleu-gris, traînée sous le titre.

**Risque :** l'Ambre sur bleu-gris peut virer au kitsch ; désaturer, valider AA sur corps et liens.
