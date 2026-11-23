# The Broadside

Tagline : Pull the press lever and ink crosses the columns; cut the proof from the paper to read what was actually printed.

Palette : Charbon `#171614` (atelier d'imprimerie) ; Oxblood `#78232A` (encre du tampon, filet de titre) ; Or `#C8A44C` (règles de laiton, focus) ; Parchemin `#E7DAB9` (papier, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et le grand titre du placard ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait en colonnes et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Un placard encadré de filets, un titre large et trois colonnes séparées par des règles ; le levier à gauche fait venir l'encre dans les colonnes, puis un talon détaché porte la preuve. En-tête discret, preuve et retour sous le placard.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Broadside                                      │
│ ═══════════════════════════════════════════════     │
│  The first chapter, set in type                    │
│  │ « A gaudy and dazzling … » │   │   │             │  ← 3 colonnes
│ ═══════════════════════════════════════════════     │
│  ( levier )  [ Cut the proof EV-0001-001 ]          │  ← preuve + retour
│  - - - - - - - - - - - - - - - - - - - - - -         │
│  The sound asleep Zhou Mingrui …   ← talon détaché │
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur abaisse le levier de la presse (clic, Entrée ou Espace) ; un rouleau traverse le placard et l'extrait du chapitre un apparaît en encre dans les colonnes, puis « Cut the proof » avec le sceau `EV-0001-001` détache un talon portant le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Set the type again » recommence ; le rouleau est `aria-hidden`, le levier et les commandes sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime le passage du rouleau.

Voix : Des notes d'imprimeur en sentence case : « Pull the press lever », « The ink has taken », « Cut the proof », « Set the type again ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse d'imprimer un titre de journal inventé, une date, un auteur ou un fait non fourni ; les colonnes ne contiennent que l'extrait donné. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant l'impression. Refuse de séparer le sceau `EV-0001-001` de sa référence.
