# The Spiral Stair

Tagline : One tread at a time the stair winds inward, and the crimson landing stops the climb at chapter one.

Palette : Charbon `#161412` (fond, pierre de l'escalier) ; Oxblood `#6A2027` (palier cramoisien, cire du sceau) ; Or `#C9A64C` (marcheur, contours de la spirale, focus) ; Parchemin `#E6D8B7` (extrait, gloss littéral, libellés).

Typographie : Cormorant roman porte la marque, le titre et le nom du palier ; son italique est réservé à la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes, le repère de navigation et les numéros de marche. Deux familles seulement, chargées via `@font-face` local, aucune police distante.

Layout : Une spirale dessinée en traits fins occupe le centre et constitue l'unique geste fort ; un petit marcheur doré la remonte marche par marche. En-tête discret en haut, extrait et preuve en bande basse, tout le reste calme.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Spiral Stair                                   │
│            ╭───╮                                    │
│         ╭──╯   ╰──╮   ◌ marcheur (geste)           │
│        │    ●      │  ← palier cramoisien           │
│         ╰──╮   ╭──╯                                │
│            ╰───╯                                    │
│          Take the next step                         │
│  « A gaudy and dazzling dreamworld … »              │  ← extrait réel
│       [ Read the inscription EV-0001-001 ]          │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur pose le marcheur sur une marche ou avance d'une marche (pointeur, flèches du clavier) ; la spirale se parcourt jusqu'au palier cramoisien du chapitre un, seul endroit où l'extrait se déverrouille. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Descend the stair » ramène le marcheur en bas ; la spirale, les marches et le marcheur sont `aria-hidden`, les cibles de marche font 44 px, le focus est un anneau d'or, et `prefers-reduced-motion` supprime le glissement du marcheur.

Voix : Des indications de montée en sentence case : « Take the next step », « The stair holds at chapter one », « Read the inscription », « Descend the stair ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée au libellé.

Refus : Refuse d'être une spirale décorative que l'on regarde tourner — chaque marche est un déplacement réel et l'extrait reste verrouillé ailleurs ; refuse la liste de chapitres en colonne, le cadran de laiton, le dégradé généralisé, les particules et les cartes arrondies identiques. Refuse d'inventer des noms d'entités, des titres d'Arcane ou des faits hors du chapitre un, et de séparer le sceau `EV-0001-001` de sa référence.
