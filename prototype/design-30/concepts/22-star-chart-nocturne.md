# Star Chart Nocturne — *The Silent Atlas*

Carte d'étoiles : bleu nuit encre, argent, constellations fines, silence. Occulte céleste, précis et mutique.

**Palette :** Nocturne `#0A1226` (fond), Encre `#060B18` (panneaux), Argent `#D6DEE8` (titres), Poussière `#8E9BB0` (texte), Éclat `#AFC4E3` (accent).

**Typographie :** Cormorant Garamond, corps 16px/1.75 ; titres en capitales espacées, chiffres tabulaires, interlettrage large.

**Motif custom :** tracé de constellation SVG — nœuds argent reliés par des filets fins, grille céleste en filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = constellation SVG, `radial-gradient` nuitprofond, `opacity:.09` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = cartouche d'étoile : fond Encre, filet Argent 1px, repère Éclat en petites capitales.
3. `.entity` : `::before` grille en `repeating-linear-gradient` orthogonal, titre Argent, halo `text-shadow` Éclat — ni icône ni lore.

**Risque :** les filets fins disparaissent en écran dense ; épaissir à 1px et valider AA sur Poussière et liens.
