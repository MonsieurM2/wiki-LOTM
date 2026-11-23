# The Apothecary's Ledger

Tagline : Decant the tincture to the marked line and the prescription finally reads itself.

Palette : Charbon `#171310` (fond, bois du meuble, ombre des flacons) ; Oxblood `#57171F` (teinture dans le verre, cire du sceau, filet de l'étiquette) ; Or `#C7A24A` (traits de graduation, lettrage du dosage, anneau de focus) ; Parchemin `#E5D7B4` (papier du registre, extrait, gloss littéral, libellés).

Typographie : Cormorant porte la voix « apothicaire » — roman pour les noms d'entités et les titres d'ordonnance tracés à la plume, italic réservé aux étiquettes manuscrites des flacons (seul usage de l'italique, pas une troisième famille). Spectral 400 porte le corps, l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, toutes deux chargées via `@font-face` depuis les fichiers locaux (`cormorant-roman`, `cormorant-italic`, `spectral-400`, `spectral-500`), aucune police distante.

Layout : Une page de registre ouverte occupe le centre, le flacon mesureur gradué étant l'unique geste fort — en-tête discret en haut, bande d'extrait et sceau de preuve en bas, le tout calme. Les flacons, leurs étiquettes et les graduations sont dessinés en traits fins et en panneaux CSS (aucun dégradé décoratif, aucun bitmap) ; la teinture oxblood ne monte que dans le seul flacon measureur, et l'extrait reste masqué jusqu'à ce que le niveau atteigne la ligne marquée.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                 Volume one    │  ← marque + repère
├───────────────┬────────────────────────────────────┤
│  ⌁ flacons    │  Ordonnance — Crimson                │
│   ⌁  ⌁  ⌁     │   ┌──────┐  ↑ ligne marquée          │
│   ⌁  ⌁  ⌁     │   │ ▓▓▓▓ │  ← teinture (geste)       │
│  étiquettes   │   │ ▓▓   │                            │
│  manuscrites  │   └──────┘  flacon mesureur           │
├───────────────┴────────────────────────────────────┤
│  « A gaudy and dazzling dreamworld … shattering. »   │  ← extrait réel (masqué)
│     [ sceau EV-0001-001 ]  ‹ Return to the ledger    │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur décanite la teinture oxblood du flacon-source dans l'unique flacon mesureur (glisser ou toucher, Entrée/Espace au clavier) jusqu'à ce que le niveau atteigne la ligne marquée — ce dosage, et lui seul, fait apparaître l'extrait comme ordonnance rédigée — puis il presse le sceau de cire `EV-0001-001` pour lire en regard le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, avant de revenir au registre par « Return to the ledger » qui vide le flacon ; le flacon et le sceau sont des cibles de 44 px, le focus est un anneau d'or, les flacons d'étagère et les graduations décoratives sont `aria-hidden`, et `prefers-reduced-motion` supprime la montée animée du liquide (le remplissage devient instantané).

Voix : Des annotations de registre en sentence case, comme un apothicaire qui dicte une ordonnance — courtes, précises, jamais en majuscules, jamais de séparateurs « A · B · C » ni de flèches collées : « Decant to the line », « Read the label », « Break the seal », « Return to the ledger ».

Refus : Refuse d'être une jolie pharmacie décorative où les flacons seraient un simple fond — le flacon mesureur est le seul chemin d'accès au texte. Refuse la rangée de flacons tous cliquables, l'étagère pleine, la nébuleuse photo plein écran, les dégradés généraux, les particules et les cartes arrondies identiques. Refuse d'afficher l'extrait par défaut, d'inventer un nom de remède, un titre d'Arcane ou un nom de personnage d'une autre œuvre, d'employer la moindre majuscule dans les libellés, et de séparer le gloss de sa référence : la preuve `EV-0001-001` reste solidaire de l'ordonnance « Crimson », illisible sans que le flacon n'ait d'abord été rempli à la ligne.
