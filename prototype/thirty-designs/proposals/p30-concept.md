# The Wayfinder's Map

Tagline : Follow the beacons across the contours until the first one gives up its chapter.

Palette : Charbon `#141315` (fond et lignes de niveau) ; Oxblood `#7C242C` (le jalon allumé, le sceau de la preuve) ; Or `#CBA548` (les points lumineux, la route, le focus) ; Parchemin `#E8D9B7` (extrait, gloss et repères).

Typographie : Cormorant roman porte la marque, le titre et les numéros des jalons ; son italique porte seulement la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Un champ de courbes de niveau schématique contient six jalons ; en choisir un trace une route pointillée depuis le camp et l'allume, le premier jalon rendant l'extrait lisible au-dessus de la preuve et du retour.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Wayfinder's Map                                │
│   ╭──────── contour field ──────────╮  ✧ N         │
│   │  ~~~~~  1 ┄┄┄┄ 2               │  ← jalons    │
│   │ ~~~~~~~        3               │    + route   │
│   │  ~~~~~  6 ┄┄┄┄ 4               │  ← geste     │
│   │     ~~~~~    5                 │              │
│   ╰─────────────────────────────────╯              │
│   « A gaudy and dazzling dreamworld … »            │  ← extrait
│ [ Read the waypoint note EV-0001-001 ] [ Fold ]    │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur choisit un jalon (Entrée ou Espace au clavier) ; une route pointillée se trace depuis le camp et le point s'allume, seul le premier jalon rend l'extrait lisible, puis « Read the waypoint note » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Fold the map » éteint la route ; courbes, boussole et route sont `aria-hidden`, les jalons sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime l'apparition animée de la route.

Voix : Des notes de terrain en sentence case : « Choose a beacon », « The first beacon answers », « Read the waypoint note », « Fold the map ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de prétendre à une géographie ou à un trajet canonique : courbes, jalons et boussole sont un dispositif original, sans nom de personnage ni d'Arcane. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et la lecture de coordonnées comme réponse. Refuse de séparer le sceau `EV-0001-001` de sa référence.
