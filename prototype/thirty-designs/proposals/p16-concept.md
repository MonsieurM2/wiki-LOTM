# The Library of Doors

Tagline : Open the crimson door and the first chapter waits on the other side of the threshold.

Palette : Charbon `#131211` (bibliothèque, boiserie sombre) ; Oxblood `#6B1F26` (la porte du chapitre un) ; Or `#C6A24A` (poignées, seuil, focus) ; Parchemin `#E5D6B2` (extrait, glose, numéros de porte).

Typographie : Cormorant roman porte la marque, le titre et les numéros de porte ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Une enfilade de portes en légère perspective, chacune un panneau de bois à poignée de laiton ; la porte oxblood du chapitre un s'ouvre sur un seuil où apparaît l'extrait. En-tête discret, preuve et retour sous l'enfilade.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Library of Doors                               │
│   ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐                         │
│   │  │ │  │ │● │ │  │ │  │  ← porte oxblood + poignée│
│   │  │ │  │ │  │ │  │ │  │                         │
│   └──┘ └──┘ └──┘ └──┘ └──┘  ← seuil                │
│      « A gaudy and dazzling … »  ← derrière la porte │
│   [ Read the inscription EV-… ]  [ Close the door ]  │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur pousse la porte oxblood du chapitre un (clic, Entrée ou Espace) ; elle pivote sur ses gonds et laisse voir, sur le seuil, l'extrait du chapitre un. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Close the door » referme le battant ; les autres portes et le seuil sont `aria-hidden`, la poignée est une cible de 44 px au focus doré, et `prefers-reduced-motion` supprime la rotation animée du battant.

Voix : Des indications de bibliothèque en sentence case : « Open the crimson door », « The threshold holds chapter one », « Read the inscription », « Close the door ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refuse : Refuse d'attribuer les portes à des chapitres ou des entités canoniques vérifiées, les noms de personnages issus d'autres œuvres et les titres d'Arcane non vérifiés. Refuse le dégradé décoratif, les particules, les cartes arrondies identiques et l'extrait visible derrière une porte fermée. Refuse de séparer le sceau `EV-0001-001` de sa référence : le gloss reste caché jusqu'à l'ouverture de la porte.
