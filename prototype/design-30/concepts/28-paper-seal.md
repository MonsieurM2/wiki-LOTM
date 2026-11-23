# Paper and Seal — *The Notarial Archive*

Papier brun fibreux, cire rouge à cacheter, letterpress, archives notariales scellées : occulte administratif, matière et poids.

**Palette :** Cuir `#1C120C` (fond), Kraft `#332318` (panneaux), Parchemin `#D9C6A5` (texte, titres), Cire `#9E2A1F` (sceaux), Fumée `#7A6650` (filets, liens).

**Typographie :** Libre Baskerville, corps 16px/1.7 ; titres en capitales espacées, chiffres elzéviriens.

**Motif custom :** sceau de cire SVG — disque irrégulier coulé, anneau de presse, monogramme géométrique neutre ; filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = sceau SVG, dégradé Cire/Parchemin, `opacity:.08`, rotation 9deg derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = feuille Kraft : fond fibreux en `repeating-linear-gradient` diagonal, liseré Parchemin, ombre de presse `inset`.
3. `.entity` : `::before` pastille de cire Cire, titre Parchemin en capitales ; ni icône ni lore inventé.

**Risque :** la fibre peut devenir bruit ; garder le gradient sous 4% d'opacité, valider AA sur Fumée.
