# The Instrument Panel

Tagline : Set the brass needle to a graduation and read the line that the first one carries.

Palette : Charbon `#141315` (fond et cadrans au repos) ; Oxblood `#7C242C` (l'aiguille arrêtée, le moyeu, le sceau de la preuve) ; Or `#CBA548` (graduations, aiguille, rivets, focus) ; Parchemin `#E8D9B7` (chiffres, extrait, glose).

Typographie : Cormorant roman porte la marque, le titre et les chiffres des graduations ; son italique porte seulement la référence `Volume 1, chapter 1 — Crimson`. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les étiquettes d'instruments, l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Un panneau de laiton rectangulaire porte trois petits cadrans fixes et un grand cadran central dont l'aiguille balaie six graduations ; seule la première rend l'extrait lisible, avec la preuve et le retour en dessous.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Instrument Panel                               │
│ ┌─ rivets ───────────────────────────────────────┐ │
│ │  ◎ tension   ◎ drift    ◎ index                │ │  ← cadrans calmes
│ │        ╭──────────────╮                        │ │
│ │        │   / aiguille  │  ← geste signature    │ │
│ │        ╰──────────────╯                        │ │
│ │        1  2  3  4  5  6   (graduations)         │ │
│ └────────────────────────────────────────────────┘ │
│   « A gaudy and dazzling dreamworld … »            │  ← extrait
│ [ Read the calibration EV-0001-001 ] [ Return ]    │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur choisit une graduation (Entrée ou Espace au clavier) ; l'aiguille de laiton balaie le cadran et s'arrête dessus, seule la première rend l'extrait lisible, puis « Read the calibration » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Return the needle » remet l'aiguille au repos ; graduations et cadrans secondaires sont `aria-hidden`, les commandes sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime le balayage animé.

Voix : Des consignes d'atelier en sentence case : « Set the needle », « The needle rests at one », « Read the calibration », « Return the needle ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de suggérer un mécanisme canonique ou un instrument officiel ; cadrans, graduations et étiquettes sont un dispositif original. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant le choix de la première graduation. Refuse de séparer le sceau `EV-0001-001` de sa référence.
