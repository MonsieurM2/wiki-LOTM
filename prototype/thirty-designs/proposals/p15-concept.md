# The Mirror Gallery

Tagline : Touch the glass and the gallery answers in reflection, showing the same sentence on both walls.

Palette : Charbon `#151517` (salle, cadre) ; Oxblood `#742129` (liseré du miroir, verre teinté) ; Or `#CDA94F` (trainedure, reflet, focus) ; Parchemin `#E8DABA` (extrait, glose, nom reflété).

Typographie : Cormorant roman porte la marque, le titre et le nom reflété ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Une galerie strictement symétrique, deux panneaux de part et d'autre d'une fine trainedure centrale, avec un verre ovale au milieu ; toucher le verre allume les deux panneaux en miroir. En-tête centré, preuve et retour sous la galerie.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│            The Mirror Gallery                      │
│   ┌──────────┐  ╭──╮  ┌──────────┐                 │
│   │ Zhou …   │  │verre│ │ … uiM rauhZ│  ← reflet    │
│   │ « A gaudy…» │ ╰──╯  │ »…yadua A «│                 │
│   └──────────┘        └──────────┘                 │
│   [ Read the inscription EV-… ]  [ Leave the glass ] │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur touche le verre central (clic, Entrée ou Espace) ; les deux panneaux s'illuminent et l'extrait du chapitre un apparaît à gauche, son reflet inversé à droite, comme deux versions d'une même vitre. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Leave the glass » éteint la galerie ; le reflet inversé est `aria-hidden`, le verre est une cible de 44 px au focus doré, et `prefers-reduced-motion` supprime le fondu d'illumination.

Voix : Des cartels de galerie en sentence case : « Touch the glass », « The walls answer », « Read the inscription », « Leave the glass ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de présenter les reflets comme des alias ou des identités canoniques vérifiées — c'est le même nom répété par le verre, jamais une affirmation d'identité inventée. Refuse les noms de personnages issus d'autres œuvres, les titres d'Arcane non vérifiés, le dégradé décoratif, les particules, les cartes arrondies identiques et l'extrait lisible avant le geste. Refuse de séparer le sceau `EV-0001-001` de sa référence.
