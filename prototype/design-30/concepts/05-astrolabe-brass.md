# Astrolabe Brass — *Engraved Orrery*

Atelier d'instruments : laiton gravé, noir d'atelier, crème de papier, rigueur occultiste.

**Palette :** Atelier `#141210` (fond), Laiton `#B08A3E` (filets), Gravage `#7A5C2C` (accents), Crème `#EDE4D0` (texte), Patine `#3E5C50` (surlignage occulte).

**Typographie :** EB Garamond — empattements taillés comme au burin ; corps 17px/1.65, titres en petites capitales espacées, chiffres en tabulaire pour les degrés.

**Motif custom :** astrolabe SVG en filigrane — disque gradué à 36 encoches, deux cercles concentriques et une alidade en croix, tracé au trait fin — ornement global unique, jamais par fiche.

**Décisions :**
1. `.gloss` cadré d'un double filet laiton (`border-left: 3px double`), fond noir d'atelier éclairci.
2. `.entity` souligné d'un tiret laiton pointillé, `text-emphasis` au survol.
3. `.brand-mark` devient l'astrolabe SVG en filigrane, `opacity:.12`, derrière l'en-tête.

**Risque :** le laiton sur noir peut virer au doré clinquant ; désaturer et valider AA sur le corps.
