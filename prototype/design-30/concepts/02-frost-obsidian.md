# Frost Obsidian — *Cold Moon*

Obsidienne glaciale, bleu nuit presque noir, cristaux d'argent et lune froide ; géométrie anguleuse.

**Palette :** Obsidienne `#0B1018` (fond), Nuit `#141E2E` (panneaux), Argent `#B8C6D6` (filets), Lune `#E6EDF5` (texte), Givre `#6FA8C4` (accent occulte).

**Typographie :** Spectral — empattements nets, presque gravés dans la glace ; corps 17px/1.7 justifié pour la lecture longue, titres en capitales espacées et interlettrées.

**Motif custom :** cristaux anguleux en SVG — facettes losanges imbriquées, arêtes argentées sur fond nuit, générées en `repeating-conic-gradient` ; ornement global diffus en filigrane, jamais par fiche.

**Décisions :**
1. `.gloss` en panneau biseauté : `clip-path` à coin coupé, bordure givre d'un pixel, fond Nuit.
2. `.entity` d'un soulignement argent en diamant (`background` linéaire en chevrons), virant au Givre au survol.
3. `.brand-mark` remplacé par un cristal SVG à facettes, `opacity:.12`, derrière l'en-tête.

**Risque :** le bleu givre sur nuit reste bas en contraste ; valider AA sur le corps et les gloses.
