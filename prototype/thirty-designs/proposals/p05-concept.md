# The Tarot Table

Tagline : Lay the cards, draw the one that holds the chapter, and let the table give up its text.

Palette : Charbon `#15110F` (fond, feutrine de la table, ombre des cartes) ; Oxblood `#5C1A22` (dos de la carte tirée, cire du sceau, liseré de la carte active) ; Or `#C9A44C` (sigles originaux, filets des cartes, anneau de focus) ; Parchemin `#E6D7B5` (recto des cartes, extrait, gloss littéral, libellés).

Typographie : Cormorant porte la voix « consultation » — roman pour les noms d'entités et les chiffres de volume gravés sur le recto des cartes, italic réservé aux courtes légendes des sigles dessinés à la main (seul usage de l'italique, pas une troisième famille). Spectral 400 porte le corps, l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, toutes chargées via `@font-face` depuis les fichiers locaux (`cormorant-roman`, `cormorant-italic`, `spectral-400`, `spectral-500`), aucune police distante.

Layout : Une table de consultation vue de dessus, avec quatre cartes posées à plat et une seule carte centrale à tirer — ce tirage est l'unique geste fort ; en-tête discret en haut, bande d'extrait et sceau de preuve en bas, le tout calme. Les cartes sont des panneaux CSS à filets fins et à sigles géométriques originaux (aucun dégradé décoratif, aucun bitmap, aucune iconographie de tarot recopiée) ; l'extrait reste masqué jusqu'à ce que la carte centrale soit retournée.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                 Volume one    │  ← marque + repère
├────────────────────────────────────────────────────┤
│      ┌───┐        ┌───┐        ┌───┐                │
│      │ ◇ │        │ ◯ │        │ △ │                │
│      └───┘        └───┘        └───┘   ← cartes posées
│              ┌───────────┐                          │
│              │    ✦      │  ← carte à tirer (geste) │
│              └───────────┘                          │
│  « A gaudy and dazzling dreamworld … shattering. »   │  ← extrait réel (masqué)
│     [ sceau EV-0001-001 ]  ‹ Return to the table     │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur tire la carte centrale (clic ou toucher, Entrée/Espace au clavier) — ce retournement, et lui seul, fait apparaître l'extrait comme lecture du chapitre — puis il presse le sceau de cire `EV-0001-001` pour lire au dos de la carte le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, avant de revenir à la table par « Return to the table » qui repose la carte ; la carte et le sceau sont des cibles de 44 px, le focus est un anneau d'or, les sigles décoratifs sont `aria-hidden`, et `prefers-reduced-motion` supprime l'animation de retournement (le recto devient instantané).

Voix : Des paroles de table en sentence case, comme un lecteur qui tire une carte et l'énonce à haute voix — courtes, précises, jamais en majuscules, jamais de séparateurs « A · B · C » ni de flèches collées : « Draw a card », « Turn the card », « Break the seal », « Return to the table ».

Refus : Refuse d'être un joli étalage de cartes décoratif où le tirage ne serait qu'un fond — la carte tirée est le seul chemin d'accès au texte. Refuse toute iconographie de tarot recopiée (Rider-Waite ou autre jeu commercial), les prédictions et les significations divinatoires inventées, la carte stellaire concurrente, la nébuleuse photo plein écran, les dégradés généraux, les particules et les cartes arrondies toutes identiques. Refuse d'afficher l'extrait par défaut, d'inventer un titre d'Arcane, un nom de personnage issu d'une autre œuvre de l'auteur ou une signification canonique aux sigles, d'employer la moindre majuscule dans les libellés, et de séparer le gloss de sa référence : la preuve `EV-0001-001` reste solidaire de la carte « Crimson », illisible sans que la carte n'ait d'abord été tirée.
