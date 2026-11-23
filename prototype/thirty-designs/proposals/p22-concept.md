# The Ritual Circle

Tagline : Turn the outer ring until chapter one meets the pointer, then read the line the sigil guards.

Palette : Charbon `#141315` (pierre sombre) ; Oxblood `#7C242C` (le nœud du chapitre un, le trait central) ; Or `#CBA548` (anneaux, pointeur, focus) ; Parchemin `#E8D9B7` (extrait, glose, chiffres).

Typographie : Cormorant roman porte la marque, le titre et le chiffre du nœud ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Un grand cercle à trois anneaux fins, huit nœuds numérotés sur l'anneau extérieur, un pointeur fixe en haut et un sigil original immobile au centre ; l'extrait apparaît sous le cercle quand le nœud du chapitre un atteint le pointeur. En-tête discret, preuve et retour en bas.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Ritual Circle                                  │
│               ▲ pointer                            │
│           ╭──( 1 )──╮                              │
│        8 ╱    ◇     ╲ 2      ← anneaux + sigil      │
│         ╲            ╱                             │
│           ╰──( 5 )──╯                              │
│      « A gaudy and dazzling dreamworld … »         │  ← extrait
│    [ Read the inscription EV-0001-001 ] [ Unwind ]  │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur clique sur un nœud de l'anneau (Entrée ou Espace au clavier) ; l'anneau tourne jusqu'à l'amener au pointeur, et seul le nœud du chapitre un rend l'extrait lisible, puis « Read the inscription » avec le sceau `EV-0001-001` donne le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, et « Unwind the circle » repose l'anneau ; les anneaux et le sigil sont `aria-hidden`, les huit nœuds sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime la rotation animée.

Voix : Des consignes de cérémonie en sentence case : « Turn the ring », « Chapter one meets the pointer », « Read the inscription », « Unwind the circle ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de copier un sigil officiel ou d'affirmer que le cercle, les nœuds ou leur nombre appartiennent au canon ; le dessin est original et hors canon. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant l'alignement. Refuse de séparer le sceau `EV-0001-001` de sa référence.
