# The Dream Diary

Tagline : Hold a drifting fragment still and the first chapter settles into legibility for a moment.

Palette : Charbon `#141315` (chambre sans lumière) ; Oxblood `#7B2430` (le fragment crimson, le liseré du rêve) ; Or `#CCA851` (filets, focus, écriture) ; Parchemin `#E9DAB9` (fragments, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et les fragments flottants ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Une page de journal où plusieurs fragments flous dérivent en diagonale ; en retenir un le Ramène au centre et le rend net, faisant apparaître l'extrait. En-tête discret, preuve et retour sous la page.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Dream Diary                                    │
│   (a clock with no hands)                          │
│            (the crimson fragment)  ← geste          │
│        (a staircase of water)                      │
│      « A gaudy and dazzling dreamworld … »         │  ← extrait
│   [ Read the margin EV-0001-001 ] [ Let it drift ]  │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur choisit le fragment crimson parmi les fragments flous (clic, Entrée ou Espace) ; il se fixe au centre, devient net et livre l'extrait du chapitre un, puis « Read the margin » avec le sceau `EV-0001-001` donne le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, et « Let it drift » recommence ; les autres fragments sont des boutons de 44 px au focus doré, le flou est purement décoratif et `prefers-reduced-motion` supprime la dérive animée.

Voix : Des notes de journal en sentence case : « Hold the crimson fragment », « It slips away », « Read the margin », « Let it drift ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refuse : Refuse d'attribuer les fragments à une entité canonique, d'inventer un rêve de personnage ou de suggérer un contenu hors du chapitre fourni. Refuse le fond clair, la nébuleuse photo, les particules, le dégradé décoratif, les cartes arrondies identiques et un extrait lisible avant le geste. Refuse de séparer le sceau `EV-0001-001` de sa référence.
