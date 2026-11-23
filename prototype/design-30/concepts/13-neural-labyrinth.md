# Neural Labyrinth — *The Cortex Thread*

Labyrinthe occulte moderne : violet froid, réseau de fines lignes, nœuds lumineux, géométrie labyrinthique.

**Palette :** Nuit `#0B0A17` (fond), Améthyste `#D9D0F5` (titres, texte), Violet `#8B6FD4` (filets, réseau), Éclat `#B9A0FF` (nœuds, accents), Brume `#58527A` (liens, bordures).

**Typographie :** Space Grotesk, corps 16px/1.6 ; titres en capitales fines espacées, index en IBM Plex Mono tabulaire.

**Motif custom :** labyrinthe SVG — fines lignes orthogonales en réseau, nœuds lumineux aux intersections, filigrane global unique, jamais par fiche.

**Décisions :**
1. `.gloss` = labyrinthe : `::before` grillage via `repeating-linear-gradient`, fond Nuit, filet Brume.
2. `.entity` : titre Améthyste, nœud Éclat en `::before` (point + halo `box-shadow`), aucune icône.
3. `.brand-mark` devient le labyrinthe SVG en filigrane, `opacity:.08`, pulsation minimale des nœuds derrière l'en-tête — aucun logo copié.

**Risque :** le grillage peut nuire à la lisibilité ; contraste AA et `prefers-reduced-motion` à valider.
