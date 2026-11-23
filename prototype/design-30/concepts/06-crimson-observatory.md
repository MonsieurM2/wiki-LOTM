# Crimson Observatory — *Blood Moon Transit*

Observatoire carmin : oxblood saturé, nuit d'encre, réticule de télescope, lune rouge.

**Palette :** Oxblood `#3B0A12` (fond), Nuit `#0A0709` (panneaux), Carmin `#C23642` (traits), Lune `#E8C4BA` (texte), Vue `#7E2A32` (surlignages).

**Typographie :** Spectral — empattements fins de plaque gravée, corps 17px/1.6, titres en capitales espacées, chiffres tabulaires pour les coordonnées.

**Motif custom :** réticule SVG — cercle gradué, croisée fine et lune éclipsée décalée, unique en filigrane global, jamais par fiche.

**Décisions :**
1. `.sections` devient une règle de focalisation : `border-bottom: 1px solid` carmin, `.current` coiffé d'un losange SVG.
2. `.margin` cadrée en champ d'oculaire (`::before` vignetté), `.gloss-label` en lecture de coordonnées tabulaire.
3. `.proofable` révèle un soulignement carmin pointillé au survol ; `.continue` se termine par une croix de visée SVG.

**Risque :** le carmin sur oxblood rétrécit le contraste des accents ; vérifier AA sur le corps.
