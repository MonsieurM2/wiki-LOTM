# The Crypt of Names

Tagline : Draw your hand across the stone and a rubbing gives the buried sentence back.

Palette : Charbon `#151312` (fond de la crypte, pierre non gravée) ; Oxblood `#632027` (cire du sceau, veine de la stèle choisie) ; Or `#C7A24D` (lettres gravées, arête de la pierre, focus) ; Parchemin `#E4D6B6` (frottage, gloss littéral, libellés).

Typographie : Cormorant roman porte la marque, le titre et les chiffres des stèles ; son italique porte la seule référence `Volume 1, chapter 1 — Crimson`, gravée au-dessous du gloss. Spectral 400 porte l'extrait gravé et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Une rangée de stèles debout contre le mur, toutes muettes sauf une, plus large, qui concentre le seul geste fort :le frottage. L'extrait est gravé dans cette pierre et se révèle sous la main ; le gloss et le retour restent en bande basse, calmes.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Crypt of Names                                 │
│   ▯  ▯  ┌─────────────────┐  ▯  ▯                   │
│   ▯  ▯  │ « A gaudy and…»  │  ▯  ▯   ← frottage      │
│         └─────────────────┘                         │
│            Draw across the stone                   │
│  [ Read the inscription EV-0001-001 ]               │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur presse la stèle centrale et la traverse de gauche à droite (pointeur ou doigt), ou presse Entrée au clavier ; le texte gravé apparaît uniquement sous son passage, comme un frottage, et l'extrait complet devient lisible quand le geste couvre la pierre. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Return to the crypt » efface le frottage ; les stèles muettes et l'arête décorative sont `aria-hidden`, la stèle active est une cible de 44 px au minimum avec un focus doré, et `prefers-reduced-motion` supprime le fondu de révélation.

Voix : Des gestes de conservation en sentence case, sans emphase : « Draw across the stone », « The rubbing is legible », « Read the inscription », « Return to the crypt ». Pas de majuscules décoratives, pas de séparateur « A · B · C », pas de flèches collées.

Refus : Refuse d'être un cimetière de noms inventés — les stèles latérales restent anonymes et décoratives, aucun nom d'entité n'est fabriqué, aucun titre d'Arcane n'est inventé, aucun fait n'est ajouté au chapitre un. Refuse l'extrait affiché d'emblée, les cartes arrondies identiques, le dégradé généralisé, les particules et le fond clair. Refuse de séparer le sceau `EV-0001-001` de sa référence : le gloss reste caché tant que le frottage n'est pas complet.
