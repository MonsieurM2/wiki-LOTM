# Geometric Pathways — *The Measured Way*

Géométrie sacrée moderniste : cercles et carrés parfaits, grille fine, teal et or — occultisme de précision, froid et net.

**Palette :** Abysse `#07110F` (fond), Patine `#0E1C1A` (panneaux), Teal `#2E6B63` (traits), Or `#C9A24B` (filets), Ivoire `#DDE6E0` (texte).

**Typographie :** Outfit, corps 15px/1.75 ; titres en capitales espacées, chiffres tabulaires, interlettrage géométrique.

**Motif custom :** cercle inscrit dans un carré SVG, nœuds d'or sur grille millimétrée — ornement global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = cercle + carré SVG, filet Or 1px, `radial-gradient` teal, `opacity:.07` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = cartouche Patine, liseré Or 1px, grille en `linear-gradient` Teal 4%.
3. `.entity` : `::before` grille 24px Teal/Abysse, `::after` point d'or, filet sous le titre.

**Risque :** la grille peut moirer ; garder 4%, casser l'alignement sur mobile, valider AA sur corps et liens.
