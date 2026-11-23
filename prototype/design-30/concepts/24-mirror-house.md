# Mirror House — *The Glass Gallery*

Galerie de glaces : argent et graphite, typographie dédoublée, reflets infinis, vertige. Occulte spéculaire, froid et vertigineux.

**Palette :** Graphite `#0B0C0E` (fond), Ardoise `#16191D` (panneaux), Argent `#DDE2E6` (titres), Étain `#8A939C` (texte), Éclat `#BFC9D1` (accent).

**Typographie :** Cormorant Garamond, corps 16px/1.75 ; titres dédoublés en capitales espacées, calque fantôme décalé de 1px, chiffres tabulaires.

**Motif custom :** couloir de miroirs SVG — panneaux inclinés en perspective, reflets successifs s'effaçant, filigrane global unique, jamais par fiche.

**Décisions :**
1. `.brand-mark` = couloir SVG, `linear-gradient` argent/graphite, `opacity:.08` derrière l'en-tête — aucun logo copié, pas d'image par fiche.
2. `.gloss` = plaque de glace : fond Ardoise, filet Argent 1px, repère Éclat en petites capitales.
3. `.entity` : `::after` titre fantôme en `text-shadow` décalé, `repeating-linear-gradient` de reflets obliques — ni icône ni lore.

**Risque :** le décalage peut brouiller la lisibilité ; plafonner à 1px, valider AA sur Étain et liens.
