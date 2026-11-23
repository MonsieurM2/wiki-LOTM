# Ink and Vellum

Tagline : The page keeps its silence until the illuminated initial is pressed, and the gloss breaks the margin.

Palette : Charbon `#161311` (fond, encre, marge gauche) ; Oxblood `#5A1A22` (rubriques, lettrine, trait de la glose) ; Or `#C9A54B` (filets des colonnes, initiale enluminée, anneau de focus) ; Parchemin `#E6D8B8` (extrait, glose littérale, libellés).

Typographie : Cormorant porte la voix « manuscrit » — roman pour la lettrine monumentale et les noms d'entités, italic réservé aux rubriques de marge et à la référence (seul usage de l'italique, pas une troisième famille). Spectral 400 porte le corps strict des deux colonnes et l'extrait ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, toutes deux chargées via `@font-face` depuis les fichiers locaux fournis, aucune police distante.

Layout : Deux colonnes talles et serrées, séparées par un filet d'or fin, sous un en-tête discret ; la lettrine monumentale chevauche la colonne de gauche et constitue l'unique geste fort, la glose ne s'écrivant que dans la marge de droite. L'extrait réel occupe le bas de la colonne gauche en caractères serrés, sans encadré arrondi, sans dégradé ni bitmap.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│  ┌──────────────────┬───────────────────────────┐  │
│  │ ╔════╗           │                           │  │
│  │ ║ A  ║ gaudy and │   (marge de glose vide)   │  │  ← lettrine (geste)
│  │ ╚════╝ dazzling  │                           │  │
│  │ dreamworld …     │                           │  │
│  │ « …throbbing    │                           │  │
│  │ pain in his     │                           │  │
│  │ head … »        │                           │  │
│  └──────────────────┴───────────────────────────┘  │
│   [ EV-0001-001 ]        ‹ Return to the leaf      │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur presse la lettrine dorée « A » (cible ≥ 44 px, focus en anneau d'or) pour « allumer » la rubrique oxblood : la glose littérale « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson` s'inscrivent alors seules dans la marge de droite, solidaires du sceau `EV-0001-001` ; il revient au feuillet par « Return to the leaf ». Les filets et l'enluminure sont `aria-hidden`, et `prefers-reduced-motion` supprime tout fondu d'allumage.

Voix : Des rubriques et notes marginales en sentence case, comme un copiste qui annonce son texte — courtes, précises, jamais en majuscules, jamais de séparateurs « A · B · C », jamais de flèches collées : « Read the initial », "The gloss is rubbed in", « Return to the leaf ».

Refus : Refuse le faux manuscrit décoratif — une seule initiale enluminée, et elle est le chemin d'accès au texte, pas un ornement ; refuse la page de parchemin clair plein écran, les colonnes multiples concurrence, les lettrines rivales, les fausses citations latines, les dégradés généraux, les particules et les cartes arrondies identiques. Refuse d'afficher la glose par défaut, d'inventer un titre d'Arcane ou un nom issu d'une autre œuvre de l'auteur, d'employer la moindre majuscule dans les libellés, et de séparer la preuve `EV-0001-001` de sa référence : la glose reste illisible tant que l'initiale n'a pas été pressée.
