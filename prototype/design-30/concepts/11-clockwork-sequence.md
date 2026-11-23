# Clockwork Sequence — *The Escapement*

Horlogerie fine : laiton vieilli, noir graphite, engrenages imbriqués, ticks précis, rigueur occulte.

**Palette :** Graphite `#0E1012` (fond), Laiton `#8C6A3F` (engrenages, filets), Cadran `#E8DFC8` (titres, texte), Rubis `#9A5B3E` (pivot, accents), Acier `#6E7378` (liens, ticks).

**Typographie :** IBM Plex Sans, corps 16px/1.65 ; chiffres et index en IBM Plex Mono tabulaire, interlettrage serré.

**Motif custom :** échappement SVG — roue dentée, ancre et spiral de ressort, tracé au trait fin, engrenages engrénés en filigrane global unique, jamais par fiche.

**Décisions :**
1. `.gloss` = cadran : `::before` bande de ticks via `repeating-linear-gradient`, fond Graphite, filet Laiton.
2. `.entity` : index tabulaire Laiton devant le titre, soulignement pointillé (ticks), aucune icône.
3. `.brand-mark` devient l'échappement SVG en filigrane, `opacity:.1`, derrière l'en-tête, rotation lente.

**Risque :** rotation et laiton sur graphite peuvent distraire ou virer au doré ; `prefers-reduced-motion` et contraste AA à valider.
