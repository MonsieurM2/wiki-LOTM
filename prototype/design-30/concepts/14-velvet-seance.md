# Velvet Séance — *The Gilded Trance*

Salon spirite victorien : velours pourpre, cadres dorés sculptés, lueur de bougie, drapés lourds, occultisme feutré.

**Palette :** Velours `#2A0E24` (fond), Pourpre `#5C2246` (panneaux), Ivoire `#EDE3D2` (titres, texte), Or `#C9A24B` (cadres, accents), Suie `#7A5A6A` (liens, filets).

**Typographie :** Cormorant Garamond, corps 16px/1.7 ; titres en capitales espacées, index en petites capitales.

**Motif custom :** drapé et cadre SVG — volutes de velours et ornements dorés en coin, filigrane global unique, jamais par fiche.

**Décisions :**
1. `.gloss` = velours : `::before` drapé via `repeating-linear-gradient`, fond Velours, filet Or en double encadrement.
2. `.entity` : titre Ivoire, initiale cernée d'un cadre doré en `::before`, aucune icône.
3. `.brand-mark` devient l'ornement SVG, `opacity:.08`, halo de bougie ambre derrière l'en-tête — aucun logo copié.

**Risque :** l'Or sur Pourpre peut manquer de contraste ; AA et `prefers-reduced-motion` à valider.
