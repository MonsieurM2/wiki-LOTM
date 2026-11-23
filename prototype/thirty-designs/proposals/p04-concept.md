# Cartographer's Atlas

Tagline : Fix the point on the grid and the contour line finally gives up its chapter.

Palette : Charbon `#15120F` (fond, encre de la grille, ombre des courbes) ; Oxblood `#581923` (courbe de niveau ciblée, cire du sceau, point fixé) ; Or `#C8A34B` (traits de la grille, coordonnées, échelle, anneau de focus) ; Parchemin `#E5D7B4` (papier de la carte, extrait, gloss littéral, libellés).

Typographie : Cormorant porte la voix « cartographe » — roman pour les noms d'entités et les chiffres de volume inscrits dans la carte, italic réservé aux légendes de coordonnées tracées à la main (seul usage de l'italique, pas une troisième famille). Spectral 400 porte le corps, l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, toutes deux chargées via `@font-face` depuis les fichiers locaux (`cormorant-roman`, `cormorant-italic`, `spectral-400`, `spectral-500`), aucune police distante.

Layout : Une carte à courbes de niveau occupe toute la zone centrale, le point à fixer sur la grille étant l'unique geste fort — en-tête discret en haut, bande d'extrait et sceau de preuve en bas, le tout calme. Les courbes concentriques, la grille et l'échelle sont dessinées en traits fins et en panneaux CSS (aucun dégradé décoratif, aucun bitmap) ; une seule courbe oxblood se révèle au point fixé, et l'extrait reste masqué jusqu'à ce que la coordonnée tombe juste.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                 Volume one    │  ← marque + repère
├────────────────────────────────────────────────────┤
│  ╭──╮  ~~~~  courbes de niveau                      │
│  │+ │ ~~~~~~                                        │
│  ╰──╯~~~~~~~~  ~~~~~~~                              │
│       ~~~~ ⊕ ~~~~~~    ← point fixé (geste)         │
│    ───── échelle ─────                              │
│  « A gaudy and dazzling dreamworld … shattering. »   │  ← extrait réel (masqué)
│     [ sceau EV-0001-001 ]  ‹ Return to the atlas     │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur déplace le point sur la grille de la carte (glisser ou toucher, flèches au clavier) jusqu'à ce qu'il se verrouille sur la coordonnée marquée — ce relevé, et lui seul, fait apparaître l'extrait comme légende du chapitre — puis il presse le sceau de cire `EV-0001-001` pour lire en regard le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, avant de revenir à l'atlas par « Return to the atlas » qui relâche le point ; le point et le sceau sont des cibles de 44 px, le focus est un anneau d'or, les courbes et la grille décoratives sont `aria-hidden`, et `prefers-reduced-motion` supprime l'animation de verrouillage (le relevé devient instantané).

Voix : Des légendes de carte en sentence case, comme un cartographe qui cote un relief — courtes, précises, jamais en majuscules, jamais de séparateurs « A · B · C » ni de flèches collées : « Set the point », « Read the contour », « Break the seal », « Return to the atlas ».

Refus : Refuse d'être une jolie carte décorative où les courbes seraient un simple fond — le point à fixer est le seul chemin d'accès au texte. Refuse la carte stellaire concurrente, les multiples points cliquables, la nébuleuse photo plein écran, les dégradés généraux, les particules et les cartes arrondies identiques. Refuse d'afficher l'extrait par défaut, d'inventer une coordonnée canonique, un titre d'Arcane ou un nom de personnage d'une autre œuvre, d'employer la moindre majuscule dans les libellés, et de séparer le gloss de sa référence : la preuve `EV-0001-001` reste solidaire de la courbe « Crimson », illisible sans que le point n'ait d'abord été fixé.
