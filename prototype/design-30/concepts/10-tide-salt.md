# Tide and Salt — *The Sextant's Wake*

Occultisme maritime : teal profond, cartes marines, sel, boussole, brume salée.

**Palette :** Abysse `#07181C` (fond), Teal `#0D3B40` (panneaux), Sel `#E4E1D3` (titres, texte), Brume `#78989A` (liens, accents), Laiton `#C2A468` (filets, rose).

**Typographie :** Source Serif 4, corps 16px/1.7 ; titres en petites capitales espacées, relèvements en chiffres tabulaires.

**Motif custom :** rose des vents SVG — huit pointes, cercles gradués, rhumbs entrecroisés ; filigrane global unique, jamais par fiche.

**Décisions :**
1. `.gloss` = carte marine : `border: 1px solid` Brume, fond Abysse dégradé, coordonnées en coin via `::after`, filet Laiton.
2. `.entity` : titre souligné d'un filet Laiton ; `::first-letter` en Sel, pas d'icône.
3. `.brand-mark` remplacé par la rose SVG, `opacity:.08`, derrière l'en-tête — aucun logo copié.

**Risque :** Teal et Brume sur Abysse frôlent le seuil AA ; réserver Sel au corps, vérifier les accents.
