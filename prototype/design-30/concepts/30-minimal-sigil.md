# Minimal Sigil — *The Silent Glyph*

Ultra-minimalisme : graphite et or, vide immense, un seul sigil, silence. Typographie seule ornement, occulte par retenue.

**Palette :** Graphite `#0E0E0F`, Ardoise `#1B1B1D`, Or `#C9A961`, Cendre `#D8D5CD`, Plomb `#6E6B66`.

**Typographie :** Cormorant Garamond, corps 16px/1.8 ; titres en capitales espacées, interlignage large, chiffres elzéviriens.

**Motif custom :** sigil SVG unique — cercle barré d'un trait oblique, tracé Or d'1px, sans fioriture ; filigrane global, jamais par fiche.

**Décisions :**
1. `.brand-mark` = sigil SVG, trait Or `1px`, `opacity:.06`, centré derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = rien : marges larges, `border-left:1px` Plomb, ni ombre ni dégradé — le vide porte le sens.
3. `.entity` : `::before` point Or `2px`, titre Cendre en capitales espacées ; ni icône ni lore inventé.

**Risque :** trop de vide paraît inachevé ; garder le sigil lisible, valider AA sur Plomb.
