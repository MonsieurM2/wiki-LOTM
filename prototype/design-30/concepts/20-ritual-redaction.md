# Ritual Redaction — *The Sealed Record*

Censure rituelle : dossiers scellés, bandeaux noirs, tampon rouge administratif, machine à écrire. Occulte bureaucratique, froid et net.

**Palette :** Encre `#0B0A09` (fond), Papier `#1A1714` (panneaux), Cendre `#8C857A` (texte), Rouge `#9E2B25` (tampons), Os `#D8D2C4` (titres).

**Typographie :** Courier Prime, corps 15px/1.7 ; titres en capitales espacées, tabulaires, frappe monospace.

**Motif custom :** bandeau de censure SVG hachuré traversé d'un tampon rond — filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = tampon SVG rouge, anneau double, `opacity:.08`, rotation -7deg derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = dossier Papier, bandeau noir `repeating-linear-gradient` sur les sensibles, liseré Cendre.
3. `.entity` : `::before` tampon Rouge incliné, titre Os souligné d'un filet dense, ni icône ni lore.

**Risque :** le Rouge peut dominer ; plafonner à 8%, valider AA sur Cendre et liens.
