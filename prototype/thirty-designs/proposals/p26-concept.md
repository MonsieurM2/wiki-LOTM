# The Loom of Fate

Tagline : Throw the shuttle four times and read the line that appears in the cloth.

Palette : Charbon `#141315` (fond et navette au repos) ; Oxblood `#7C242C` (trame nouée) ; Or `#CBA548` (chaîne, navette, focus) ; Parchemin `#E8D9B7` (fils clairs, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et le compte des passes ; son italique porte seulement la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Un métier schématique montre dix fils de chaîne verticaux et quatre rangs de trame ; la navette passe alternativement de gauche à droite, chaque passage tissant un rang, et l'extrait se lit sous le tissu une fois le dernier rang fermé.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Loom of Fate                                   │
│   ▱ navette ─────────────────────────────►         │  ← geste signature
│   │ │ │ │ │ │ │ │ │ │                             │
│   ▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░   rang 1                │
│   ░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒   rang 2                │  ← chaîne et trame
│   ▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░   rang 3                │
│   ░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒   rang 4                │
│   « A gaudy and dazzling dreamworld … »            │  ← extrait
│  [ Read the weave note EV-0001-001 ] [ Unweave ]    │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur lance la navette (Entrée ou Espace au clavier) ; chaque passe tisse un rang en alternant les fils, et la quatrième rend l'extrait lisible, puis « Read the weave note » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Unweave the cloth » défait le tissu ; fils et navette sont `aria-hidden`, les commandes sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime le déplacement animé.

Voix : Des consignes d'atelier en sentence case : « Throw the shuttle », « Three passes remain », « The cloth holds the line », « Unweave the cloth ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de faire du tissage une allégorie canonique ou d'y attacher des noms de voies ; le métier et ses quatre rangs sont un dispositif original. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant la dernière passe. Refuse de séparer le sceau `EV-0001-001` de sa référence.
