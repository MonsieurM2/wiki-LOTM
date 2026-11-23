# Bakelite Deco — *Amber Dial*

Art déco 1930 : bakélite brune, cadrans de laiton, soleil géométrique rayonnant.

**Palette :** Bakélite `#2B1A12` (fond), Laiton `#B08D4F` (filets), Ambre `#D9A441` (accent), Ivoire `#EDE2CC` (texte), Oxide `#6E2C1E` (surlignage occulte).

**Typographie :** Cormorant Garamond — ses empattements fins évoquent la gravure sur cadran ; corps 17px/1.65 pour la lecture longue, titres en petites capitales espacées.

**Motif custom :** soleil rayonnant en SVG, 24 rayons alternant traits fins et trapèzes, centré sur un disque de laiton en `repeating-conic-gradient` — ornement global uniquement, jamais par fiche.

**Décisions :**
1. `.gloss` cadré d'un double filet laiton (`border-left: 3px double`) sur fond bakélite éclairci.
2. `.entity` souligné d'un tiret ambre pointillé, `text-emphasis` au survol.
3. `.brand-mark` devient le soleil SVG en filigrane, `opacity:.15`, derrière l'en-tête.

**Risque :** l'ambre sur brun frôle le contraste faible ; valider AA sur le corps de texte.
