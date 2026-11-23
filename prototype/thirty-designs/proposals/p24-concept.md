# The Choir of Voices

Tagline : Choose the voice that carries chapter one and hear the line it holds.

Palette : Charbon `#141315` (fond et têtes de notes) ; Oxblood `#7C242C` (la note choisie, le sceau de la preuve) ; Or `#CBA548` (portées, tenue de la note, focus) ; Parchemin `#E8D9B7` (taille des notes, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et les chiffres des voix ; son italique porte seulement la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les numéros de voix, l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Une portée de cinq lignes traverse la page, sept notes posées à des hauteurs différentes ; la note choisie s'emplit d'oxblood et une tenue dorée traverse la portée, l'extrait et la preuve apparaissant en dessous.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Choir of Voices                                │
│ ─────────────────────────────────────────────────   │
│ ────●───────────●───────●───────────●───────●───   │  ← portée + notes
│ ─────────────────────────────────────────────────   │
│  1      2       3       4       5       6      7   │
│ ━━━━━━━━━━━ tenue dorée ━━━━━━━━━━━━━━━━━━━━━━━━   │  ← geste signature
│   « A gaudy and dazzling dreamworld … »            │  ← extrait
│  [ Read the verse line EV-0001-001 ] [ Be silent ]  │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur choisit une note (Entrée ou Espace au clavier) ; seule la première fait résonner la portée et étend la tenue dorée, ce qui rend l'extrait lisible, puis « Read the verse line » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Be silent » éteint la portée ; les lignes et la tenue sont `aria-hidden`, les notes sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime l'animation.

Voix : Des indications de partition en sentence case : « Choose the voice that carries chapter one », « The first voice holds the line », « Read the verse line », « Be silent ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse d'attribuer une voix à un personnage réel ou d'imiter une partition canonique ; les sept notes sont un dispositif original. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant le choix de la première voix. Refuse de séparer le sceau `EV-0001-001` de sa référence.
