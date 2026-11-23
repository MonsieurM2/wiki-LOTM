# Occult Poster — *The Gilded Curve*

Affiche Art Nouveau : volutes sinueuses, ocre et noir, bordures ornementales, lettrage fondu dans l'ornement. Occulte graphique, théâtral et clos.

**Palette :** Nuit `#0B0907` (fond), Ocre brûlé `#B9741F` (volutes, filets), Or pâle `#E2B65C` (titres, bordures), Ivoire `#E7DAC0` (texte), Oxide `#6E3B18` (ombres, accents).

**Typographie :** Cormorant Garamond, corps 16px/1.7 ; titres en capitales espacées, lettrines ornées épousant la volute.

**Motif custom :** arabesque SVG en coup de fouet — tige ocre unique, vrilles symétriques, nœud central ; filigrane global, jamais par fiche.

**Décisions :**
1. `.brand-mark` = arabesque SVG, dégradé Or pâle/Ocre brûlé, `opacity:.08` en filigrane d'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = cadre d'affiche : double filet Or pâle, coins en volutes SVG, lettrage enrubanné en haut.
3. `.entity` : `::before` volute SVG avec puce-ocre, titre en capitales espacées ; ni icône ni lore inventé.

**Risque :** Or pâle sur Nuit reste lisible, mais l'Oxide sur fond sombre frôle le seuil AA — réserver aux ombres décoratives.
