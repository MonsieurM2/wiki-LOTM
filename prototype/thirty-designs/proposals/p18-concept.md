# The Telegraph Office

Tagline : Hold the brass key down and chapter one arrives as a punched strip of paper, until a wax stamp closes the line.

Palette : Charbon `#161514` (bureau, nuit) ; Oxblood `#7C242B` (cire du tampon, encre du sceau) ; Or `#C9A44E` (laiton, perforations, focus) ; Parchemin `#E6D9B8` (bande de papier, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et la mention du tampon ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait qui se déroule sur la bande et le gloss littéral ; Spectral 500 porte la clé, les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Un bureau sombre avec une clé de laiton en bas et une bande de papier perforée au-dessus ; la bande reste vide jusqu'à l'envoi, puis l'extrait s'y imprime caractère par caractère. En-tête discret, preuve tamponnée et retour sous le bureau.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Telegraph Office                               │
│  ┌ - - - - - - - - - - - - - - - - - - - - - ┐      │
│  │ « A gaudy and dazzling dreamworld … »    │      │  ← bande perforée
│  └ - - - - - - - - - - - - - - - - - - - - - ┘      │
│            ( clé de laiton )                       │
│   [ Apply the proof stamp EV-0001-001 ]            │  ← preuve + retour
│   [ Tear off the tape ]                            │
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur presse la clé de laiton (clic, Entrée ou Espace) ; la bande avance et l'extrait du chapitre un s'imprime caractère par caractère, puis il appose le tampon `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, et « Tear off the tape » efface tout ; la bande et les perforations sont `aria-hidden`, la clé et les commandes sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` imprime l'extrait d'un seul coup.

Voix : Des dépêches en sentence case : « Press the brass key », « The line is clear », « Apply the proof stamp », « Tear off the tape ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse d'inventer une dépêche, un expéditeur ou un fait hors du texte fourni ; refuse toute allégation canonique non vérifiée. Refuse le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant l'envoi. Refuse de séparer le sceau `EV-0001-001` de sa référence.
