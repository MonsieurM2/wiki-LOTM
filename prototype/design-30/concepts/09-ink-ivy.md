# Ink and Ivy — *The Pressed Herbarium*

Herbier occulte : vert-noir profond, lierre pressé, or pâle, planches séchées sous verre.

**Palette :** Encre `#0B1410` (fond), Lierre `#1D3328` (panneaux), Or pâle `#D9CFA4` (titres, texte), Mousse `#587A5C` (liens, accents), Papier `#A8A88C` (étiquettes, marges).

**Typographie :** Spectral, corps 16px/1.7 ; titres en petites capitales espacées, étiquettes d'échantillon en italique.

**Motif custom :** empreinte de lierre pressé SVG — feuille aplatie, nervures en filet fin, quelques feuilles fanées ; filigrane global unique, jamais par fiche.

**Décisions :**
1. `.gloss` = planche d'herbier : `border: 1px solid` Mousse, fond Lierre dégradé, coin replié via `clip-path`, étiquette Papier en italique.
2. `.entity` : titre souligné d'un filet Or pâle ; `::first-letter` en Or pâle, pas d'icône.
3. `.brand-mark` remplacé par l'empreinte SVG, `opacity:.09`, derrière l'en-tête — aucun logo copié.

**Risque :** Mousse et Papier sur Encre frôlent le seuil AA ; réserver Or pâle au corps, vérifier les accents.
