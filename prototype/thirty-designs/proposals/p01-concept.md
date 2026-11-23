# The Brass Orrery

Tagline : Turn the brass until a chapter crosses the sight — nothing is read until it is aligned.

Palette : Charbon `#161311` (fond, boîtier, ombre des orbites) ; Oxblood `#5A1A22` (disque de la planète alignée, cire du sceau) ; Or laiton `#C9A54B` (graduations, orbites, aiguille d'index, anneau de focus) ; Parchemin `#E6D8B8` (extrait, gloss, libellés).

Typographie : Cormorant porte la voix « instrument » — roman pour les noms d'entités et les chiffres de volume gravés au moyeu, italic réservé aux étiquettes des planètes (seul usage de l'italique, pas une troisième famille). Spectral 400 porte le corps, l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, toutes deux chargées via `@font-face` depuis les fichiers locaux, aucune police distante.

Layout : Un cadran circulaire occupe le centre et constitue l'unique geste fort ; tout le reste — en-tête discret en haut, bande d'extrait en bas — reste calme et silencieux. Les trois anneaux concentriques (volumes, chapitres, hub) sont dessinés en traits fins et en graduations CSS, sans dégradé ni bitmap ; l'aiguille d'index est fixe en haut, le texte n'apparaît que sous elle.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│                      ╭───────╮                      │
│                   ╭──┤  ☉ ◉  ├──╮                   │
│            ○    ╭─┴───────────────┴─╮    ○          │
│                 │   ○      hub       │               │  ← orrerie (geste)
│         ○      ╰─────────────────────╯      ○       │
│                      ▼ index fixe                    │
│   « A gaudy and dazzling dreamworld instantly … »    │  ← extrait réel
│        [ sceau EV-0001-001 ]   ‹ Return to the orrery│  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur fait tourner l'anneau des chapitres (glisser à la souris ou au doigt, flèches gauche/droite au clavier) jusqu'à ce que la planète oxblood s'arrête sous l'aiguille d'index — cet alignement, et lui seul, fait apparaître l'extrait — puis il presse le sceau `EV-0001-001` pour faire basculer la planète et lire au dos le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, avant de revenir au cadran par « Return to the orrery » ; les planètes sont des cibles de 44 px, le focus est un anneau d'or, les éléments décoratifs (graduations, orbites) sont `aria-hidden`, et `prefers-reduced-motion` supprime la rotation animée.

Voix : Des légendes d'instrument en sentence case, comme un registre d'observatoire ou une étiquette de musée — courtes, précises, jamais en majuscules, jamais de séparateurs « A · B · C », jamais de flèches collées : « Turn the ring », « Seal closed », « Return to the orrery ».

Refus : Refuse d'être un joli système solaire décoratif — l'orrerie est le seul chemin d'accès au texte, pas un fond ; refuse la liste défilante de chapitres, la carte stellaire concurrente, la nébuleuse photo plein écran, les dégradés généraux, les particules et les cartes arrondies identiques. Refuse d'afficher l'extrait par défaut, de prêter aux planètes des noms de Sequences ou de voies non vérifiés, d'inventer un titre d'Arcane, d'employer la moindre majuscule dans les libellés, et de séparer le gloss de sa référence : la preuve `EV-0001-001` reste solidaire de la planète « Crimson », impossible à lire sans l'avoir d'abord alignée.
