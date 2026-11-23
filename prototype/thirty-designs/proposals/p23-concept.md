# The Labyrinth Index

Tagline : Follow the dotted thread through the maze until the first chamber gives up its line.

Palette : Charbon `#141315` (fond et chambres) ; Oxblood `#7C242C` (la fausse piste, le sceau de la preuve) ; Or `#CBA548` (le fil qui se tend, la chambre atteinte, le focus) ; Parchemin `#E8D9B7` (murs, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et les chiffres des chambres ; son italique porte seulement la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte le repère de navigation, l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Un labyrinthe orthogonal au trait fin occupe un carré ; trois chambres numérotées surmontent le tracé, et le fil doré se dessine d'une entrée vers la chambre choisie tandis que l'extrait et la preuve se lisent en dessous.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Labyrinth Index                                │
│   ┌──────────────┐                                 │
│   │ ②            │                                 │  ← murs + fil pointillé
│   │   ┌──┐  ① ◄━━┥━━ fil                           │
│   │   └──┘      │                                 │
│   │          ③  │                                 │
│   └──────────────┘                                 │
│   « A gaudy and dazzling dreamworld … »            │  ← extrait
│  [ Read the margin note EV-0001-001 ] [ Wind back ] │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur choisit une chambre (Entrée ou Espace au clavier) ; le fil doré se tend le long du tracé pointillé jusqu'à elle, et seule la chambre un rend l'extrait lisible, puis « Read the margin note » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Wind the thread back » remet le fil à zéro ; les murs et le tracé sont `aria-hidden`, les chambres sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime le déroulement animé.

Voix : Des consignes de repérage calmes en sentence case : « Choose a chamber and follow the thread », « The thread reaches chamber one », « Read the margin note », « Wind the thread back ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de présenter le labyrinthe comme une structure du canon ou d'y placer des noms de personnages ; le dessin et les chambres sont originaux. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant que le fil n'atteigne la chambre un. Refuse de séparer le sceau `EV-0001-001` de sa référence.
