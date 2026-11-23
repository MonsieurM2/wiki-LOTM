# The Mask Cabinet

Tagline : Slide open a drawer and see which chapter the face underneath answers to.

Palette : Charbon `#141315` (fond, tiroirs fermés) ; Oxblood `#7C242C` (l'intérieur du tiroir, le sceau de la preuve) ; Or `#CBA548` (poignées, masque, focus) ; Parchemin `#E8D9B7` (chiffres, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et le chiffre du tiroir ; son italique porte seulement la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Un meuble à six tiroirs carrés occupe le centre ; ouvrir un tiroir fait glisser sa façade vers le haut et découvre un masque original, seul le tiroir un donnant accès à l'extrait et à la preuve en dessous.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Mask Cabinet                                   │
│  ┌────┬────┬────┐                                  │
│  │ 1  │ 2  │ 3  │   ① façade glissée                │
│  ├────┼────┼────┤   ◎ masque découvert              │
│  │ 4  │ 5  │ 6  │                                  │
│  └────┴────┴────┘                                  │
│   « A gaudy and dazzling dreamworld … »            │  ← extrait
│  [ Read the inventory slip EV-0001-001 ] [ Close ]  │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur ouvre un tiroir (Entrée ou Espace au clavier) ; la façade glisse et découvre un masque, seul le tiroir un rend l'extrait lisible, puis « Read the inventory slip » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Close the drawers » referme le meuble ; les masques sont `aria-hidden`, les tiroirs sont des cibles d'au moins 44 px au focus doré, et `prefers-reduced-motion` supprime le glissement animé.

Voix : Des consignes d'inventaire en sentence case : « Open a drawer », « Chapter one answers here », « Read the inventory slip », « Close the drawers ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de donner aux masques le nom d'un personnage ou d'un Arcane, et de copier un visuel officiel ; les masques sont originaux et sans identité canonique. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant l'ouverture du tiroir un. Refuse de séparer le sceau `EV-0001-001` de sa référence.
