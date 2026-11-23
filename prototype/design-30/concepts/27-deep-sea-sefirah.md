# Deep Sea Sefirah — *The Abyssal Sphere*

Abysse océanique : bleu quasi noir, bioluminescence cyan, courbes organiques, pression sourde.

**Palette :** Abysse `#03080F` (fond), Cuvette `#0C1E2B` (panneaux), Sève `#4FD8CE` (bioluminescence, liens), Écume `#B6F2EA` (titres, texte), Pression `#1C4650` (filets, accents).

**Typographie :** Spectral, corps 16px/1.7 ; titres en capitales espacées, chiffres tabulaires.

**Motif custom :** sphère abyssale SVG — cercle central, huit courbes tentaculaires ondulées, points lumineux ; filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = sphère SVG, dégradé Sève/Écume, `opacity:.07` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = bulle de pression : `border:1px solid` Pression, fond radial Abysse→Cuvette, halo `box-shadow` Sève, `border-radius` asymétrique.
3. `.entity` : `::before` courbe SVG cyan comme puce, titre en capitales espacées ; ni icône ni lore inventé.

**Risque :** Sève sur Abysse éblouit ; réserver Écume au corps, vérifier les accents à faible opacité.
