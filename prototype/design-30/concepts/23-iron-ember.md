# Iron and Ember — *The Forge Ledger*

Forge industrielle : fer riveté, braise orange, noir de suie, chaleur sourde. Occulte métallurgique, dense et feutré.

**Palette :** Forge `#0C0A09` (fond), Scorie `#1A1411` (panneaux), Acier `#D9D3C9` (titres), Suie `#948A80` (texte), Braise `#C85A28` (accent).

**Typographie :** Barlow Condensed, corps 16px/1.7 ; titres en capitales serrées, chiffres tabulaires, interlettrage réduit.

**Motif custom :** bande de fer rivetée SVG — rivets alignés, câble tressé, halo de braise — filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = bande rivetée SVG, `linear-gradient` braise sourde, `opacity:.08` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = plaque d'usine : fond Scorie, filet Acier 1px, numéro Braise en petites capitales.
3. `.entity` : `::before` tressage en `repeating-linear-gradient` oblique, titre Acier, halo `text-shadow` Braise — ni icône ni lore.

**Risque :** la braise peut virer au rouge vif ; plafonner l'opacité, valider AA sur Suie et liens.
