# Clocktower Noir — *The Long Shadow*

Film noir : noir d'encre, contraste dur, ombres portées nettes, amber, angles vifs, cadran de tour.

**Palette :** Goudron `#0B0B0C` (fond), Nuit `#131417` (panneaux), Amber `#E8A33D` (aiguilles, accents), Craie `#D5D0C4` (titres, texte), Ombra `#5C5A55` (liens, filets).

**Typographie :** Barlow Condensed, corps 16px/1.6 ; titres en capitales serrées, chiffres tabulaires.

**Motif custom :** cadran de tour SVG vu d'en bas — index anguleux, aiguilles triangulaires, ombre nette ; filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = cadran SVG, `opacity:.08` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = lame de lumière : `clip-path: polygon(...)`, amber sur Goudron, ombre portée `box-shadow: 6px 6px 0` sans flou.
3. `.entity` : `::before` aiguille triangulaire Amber, titre Craie en capitales ; ni icône ni lore inventé.

**Risque :** l'amber sur Goudron peut virer au jaune ; valider AA sur Ombra.
