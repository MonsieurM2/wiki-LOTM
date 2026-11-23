# Cathedral Glass — *Vespers in Lead*

Verre sombre soudé de plomb : bleu, rouge et émeraude ne s'éclairent que filtrés, jamais francs.

**Cinq verres** — Nef `#0A0910` (fond, plomb), Saphir `#3757C4` (liens), Grenat `#9E2737` (titres), Émeraude `#1B7A62` (surlignage), Étain `#E8E2D0` (texte).

**Typographie** — Cormorant Garamond, corps 16px/1.65 ; titres Cinzel en petites capitales, lettrines cerclées de plomb.

**Motif custom** — treillis de plomb SVG : losanges inégaux, nœuds de soudure aux intersections, filigrane global unique, jamais par fiche.

**Soudures (décisions)**
1. `.gloss` = panneau teinté en dégradé Joyau sur Nef, `border: 3px solid` Nef et `inset 0 0 0 1px` Étain ; `.gloss-label` en Cinzel.
2. `.sections` : `::before` came verticale, nœuds en `radial-gradient` ; `.current` reçoit un halo émeraude (`drop-shadow`).
3. `.margin` : `feTurbulence` + `feDisplacementMap` sur un `<pattern>` irrégulier ; `.continue` scellé d'un nœud SVG.

**Risque** — Grenat et Émeraude sous le seuil AA sur Nef : réserver Étain au corps, vérifier les accents.
