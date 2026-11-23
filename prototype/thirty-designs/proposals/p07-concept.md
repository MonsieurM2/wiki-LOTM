# The Clockmaker's Workshop

Tagline : The escapement holds its breath until one tooth is released, and the chapter ticks into view.

Palette : Charbon `#161311` (fond, boîtier, ombre des engrenages) ; Oxblood `#5A1A22` (dent engagée, cire du sceau) ; Or laiton `#C9A54B` (dents, échappement, anneau de focus) ; Parchemin `#E6D8B8` (extrait, gloss littéral, libellés).

Typographie : Cormorant porte la voix « atelier » — roman pour les noms d'entités et les chiffres de chapitre gravés sur les dents, italic réservé aux étiquettes de l'échappement (seul usage de l'italique, pas une troisième famille). Spectral 400 porte le corps, l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, toutes deux chargées via `@font-face` depuis les fichiers locaux fournis, aucune police distante.

Layout : Un grand engrenage avec son échappement occupe le centre et constitue l'unique geste fort ; tout le reste — en-tête discret en haut, bande d'extrait en bas — reste calme et silencieux. Les dents et l'échappement sont dessinés en traits fins et en cercles CSS, sans dégradé ni bitmap ; la dent oxblood n'apparaît qu'une fois l'échappement libéré, et le texte ne s'affiche qu'alors.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│                   ╭─────╮                           │
│                ╭──┤  ▓▓ ├──╮                        │
│             ▓▒░│  │ échap│  │░▒▓                     │  ← engrenage (geste)
│             ░  ╰──┤  ▓▓ ├──╯  ░                     │
│                ... dents ...   ▼ dent oxblood        │
│   « A gaudy and dazzling dreamworld instantly … »    │  ← extrait réel
│        [ EV-0001-001 ]   ‹ Return to the workshop    │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur libère l'échappement d'un cran (glisser sur la couronne ou au doigt, flèches gauche/droite au clavier) jusqu'à ce que la dent oxblood s'engage — cet engagement, et lui seul, fait apparaître l'extrait — puis il presse le sceau `EV-0001-001` pour faire basculer la dent et lire au dos le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, avant de revenir à l'atelier par « Return to the workshop » ; les dents sont des cibles de 44 px, le focus est un anneau d'or, les éléments décoratifs (dents, échappement) sont `aria-hidden`, et `prefers-reduced-motion` supprime le tic-tac animé.

Voix : Des étiquettes d'établi d'horloger en sentence case, comme un registre de réglage — courtes, précises, jamais en majuscules, jamais de séparateurs « A · B · C », jamais de flèches collées : « Release the escapement », « Tooth engaged », « Return to the workshop ».

Refus : Refuse d'être une jolie horloge décorative — l'échappement est le seul chemin d'accès au texte, pas un fond ; refuse la liste défilante de chapitres, le cadran de laiton concurrent, la nébuleuse photo plein écran, les dégradés généraux, les particules et les cartes arrondies identiques. Refuse d'afficher l'extrait par défaut, de donner aux dents des noms de Sequences ou de voies non vérifiés, d'inventer un titre d'Arcane ou un nom issu d'une autre œuvre de l'auteur, d'employer la moindre majuscule dans les libellés, et de séparer la preuve `EV-0001-001` de sa référence : le gloss reste illisible tant que la dent n'a pas été engagée.
