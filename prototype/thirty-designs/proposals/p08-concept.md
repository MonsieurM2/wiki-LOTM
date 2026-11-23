# The Bell Tower

Tagline : Pull the rope and the bells answer in turn until the crimson one gives up its chapter.

Palette : Charbon `#171412` (fond de la tour, ombre des cloches) ; Oxblood `#6B1F27` (la cloche cramoisie, cire du sceau) ; Or `#C9A54B` (corde, battant, anneaux de résonance, focus) ; Parchemin `#E7D9BA` (extrait, glose littérale, libellés).

Typographie : Cormorant roman porte la marque, le titre et les numéros de pas gravés près des cloches ; son italique est réservé à la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et la glose littérale ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, chargées via `@font-face` depuis les fichiers locaux fournis, aucune police distante.

Layout : Une corde verticale occupe le centre, unique geste fort de la page ; les cloches sont invisibles, suggérées par de simples anneaux qui résonnent au passage du battant. En-tête discret, extrait et preuve en bande basse, tout le reste silencieux.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Bell Tower                                     │
│   ○ 01   │                                          │
│   ○ 02   │   ← corde + battant (geste)              │
│   ● 03   ◆   ← cloche cramoisie, anneaux de son      │
│   ○ 04   │                                          │
│          Pull the rope                             │
│  « A gaudy and dazzling dreamworld instantly … »    │  ← extrait réel
│       [ Read the inscription EV-0001-001 ]          │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur tire la corde vers le bas (glisser au pointeur, touches de haut en bas au clavier) ; chaque cran fait résonner l'anneau d'une cloche invisible, et seul l'alignement avec la cloche cramoisie du chapitre un fait apparaître l'extrait. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire la glose littérale « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, puis « Climb back down » le ramène en bas de la tour ; la corde et les anneaux décoratifs sont `aria-hidden`, le focus est un anneau d'or, les crans sont des cibles de 28 px dans une zone tactile de 44 px, et `prefers-reduced-motion` supprime les ondes de résonance.

Voix : Des indications de sonnerie en sentence case, brèves et sans emphase : « Pull the rope », « A bell answers », « The crimson bell answers », « Read the inscription », « Climb back down ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée au libellé.

Refus : Refuse d'être un carillon ornemental qui joue en boucle — les cloches restent invisibles et ne sonnent qu'au geste ; refuse l'extrait affiché par défaut, la liste défilante de chapitres, le cadran de laiton, le dégradé généralisé, les particules et les cartes arrondies identiques. Refuse d'inventer un nom d'entité, un titre d'Arcane ou un fait hors du chapitre un, et de séparer le sceau `EV-0001-001` de sa référence : la glose reste illisible tant que la cloche cramoisie n'a pas été atteinte.
