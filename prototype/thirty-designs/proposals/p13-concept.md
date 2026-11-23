# The Observatory Dome

Tagline : Turn the brass rail until the crimson star crosses the meridian, and the first chapter lights up on the chart.

Palette : Charbon `#141416` (intérieur du dôme, nuit) ; Oxblood `#7A232C` (l'étoile crimson, le repère méridien) ; Or `#C9A64E` (rail de laiton, réticule, focus) ; Parchemin `#E7D8B8` (noms d'étoiles, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et les noms d'étoiles ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte le rail, les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Un dôme semicirculaire en haut, semé d'étoiles fines et traversé d'un méridien fixe ; au-dessous, un rail de laiton qu'on fait glisser, puis une plaque de relevé où apparaît l'extrait. En-tête discret, preuve et retour sous la plaque.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Observatory Dome                               │
│        ╭── ✦ ────│──── ✦ ──╮   ← dôme + méridien    │
│        │   ✦     │    ✦    │                       │
│      ═══════════════════════   ← rail de laiton     │
│      « A gaudy and dazzling … »  ← plaque de relevé │
│      [ Read the inscription EV-… ]  [ Reset ]       │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur fait glisser le rail (glisser-souris, glisser tactile, ou flèches au clavier) ; le ciel tourne jusqu'à ce que l'étoile crimson coïncide avec le méridien, ce qui fait apparaître l'extrait du chapitre un sur la plaque. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Reset the sky » recommence ; le dôme, les étoiles et le réticule sont `aria-hidden`, le rail est une cible de 44 px au focus doré, et `prefers-reduced-motion` supprime la rotation animée.

Voix : Des notes d'observatoire en sentence case : « Turn the dome », « The crimson star is on the meridian », « Read the inscription », « Reset the sky ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse une nébuleuse photographique plein écran, des constellations présentées comme des groupes de personnages canoniques vérifiés, les noms d'entités fabriqués et les titres d'Arcane non vérifiés. Refuse le dégradé décoratif, les particules, les cartes arrondies identiques et la lisibilité immédiate de l'extrait : la plaque reste vide tant que l'étoile n'est pas alignée. Refuse de séparer le sceau `EV-0001-001` de sa référence.
