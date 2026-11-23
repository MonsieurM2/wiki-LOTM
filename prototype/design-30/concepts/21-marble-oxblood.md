# Marble and Oxblood — *The Stone Gallery*

Musée de pierre : bustes de marbre, oxblood profond, étiquettes de galerie, lumière rasante. Occulte sculptural, froid et solennel.

**Palette :** Oxblood `#2B0C11` (fond), Niche `#160E10` (panneaux), Marbre `#E6E2D8` (titres), Veine `#8C8079` (texte), Rasante `#C98F6B` (accent).

**Typographie :** Cormorant Garamond, corps 16px/1.75 ; titres en capitales espacées, lettrage gravé, chiffres d'inventaire tabulaires.

**Motif custom :** profil de buste SVG traversé d'un faisceau oblique, veinure et étiquette de galerie — filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = buste SVG, `linear-gradient` oblique lumière rasante, `opacity:.08` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = étiquette de galerie : cartouche Niche, filet Marbre 1px, numéro Rasante en petites capitales.
3. `.entity` : `::before` veinure en `repeating-linear-gradient` oblique, titre Marbre, `text-shadow` rasante — ni icône ni lore.

**Risque :** Rasante peut éblouir et nuire au contraste ; plafonner l'opacité, valider AA sur Veine et liens.
