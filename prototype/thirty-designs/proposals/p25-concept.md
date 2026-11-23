# The Tide Chart

Tagline : Raise the mark of chapter one and let the flood uncover the line beneath it.

Palette : Charbon `#141315` (fond et repères) ; Oxblood `#7C242C` (la marée montante) ; Or `#CBA548` (graduations, crête, focus) ; Parchemin `#E8D9B7` (chiffres de hauteur, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et les chiffres de hauteur ; son italique porte seulement la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Une courbe de marée schématique occupe un graphique rectangulaire, six repères de chapitre alignés à droite ; le choix du repère un fait monter l'eau et l'extrait se lit sous le graphique avec sa preuve.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Tide Chart                                     │
│ ┌────────────────────────────┐                     │
│ │ 6 ────────────────         │                     │
│ │ 5 ────────────────  (2)    │                     │  ← repères + eau
│ │ 4 ────────────────         │                     │
│ │ 3 ────────────────         │                     │
│ │ 2 ────────────────  (1)◄━━━┥━━ crête oxblood    │
│ │ 1 ╱▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│                     │
│ └────────────────────────────┘                     │
│   « A gaudy and dazzling dreamworld … »            │  ← extrait
│  [ Read the sounding EV-0001-001 ] [ Let it fall ]  │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur choisit un repère de chapitre (Entrée ou Espace au clavier) ; seul le repère un fait monter la crête oxblood et rend l'extrait lisible, puis « Read the sounding » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Let the tide fall » vide le graphique ; le quadrillage et la crête sont `aria-hidden`, les repères sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime la montée animée.

Voix : Des consignes de relevé en sentence case : « Choose a chapter mark », « The first mark is under water », « Read the sounding », « Let the tide fall ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refuse : Refuse d'attribuer une hauteur de marée réelle à un chapitre ou de suggérer un cycle canonique ; les niveaux sont un dispositif original. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant la montée du repère un. Refuse de séparer le sceau `EV-0001-001` de sa référence.
