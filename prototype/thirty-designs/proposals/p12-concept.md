# The Alchemist's Notebook

Tagline : Follow the five points with your hand, and the closed figure gives back the sentence in the margin.

Palette : Charbon `#151311` (papier du cahier, reliure) ; Oxblood `#67202A` (encre du sceau, point de fermeture) ; Or `#C8A44D` (trait du pentacle, points, focus) ; Parchemin `#E5D7B6` (annotations, extrait, gloss littéral).

Typographie : Cormorant roman porte la marque, le titre et les chiffres des cinq points ; son italique porte les annotations manuscrites de la marge et la référence `Volume 1, chapter 1 — Crimson`, seuls usages de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Un cahier ouvert : à gauche le diagramme, seul geste fort de la page, à droite une marge d'annotations qui reste vide jusqu'à ce que la figure se ferme. En-tête discret, gloss et retour sous la marge.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Alchemist's Notebook                           │
│  ┌───────────┐   Trace the five points in order    │
│  │    ①      │   « A gaudy and dazzling … »        │  ← extrait réel
│  │   ☆       │                                    │
│  │  ⑤  ③     │   [ Read the inscription EV-… ]     │  ← preuve + retour
│  └───────────┘                                    │
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur touche les cinq points du diagramme dans l'ordre (pointeur ou Tab puis Entrée) ; chaque point correct trace un côté en or, un ordre erré efface le tracé, et le retour au premier point ferme la figure et fait apparaître l'extrait dans la marge. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Close the notebook » recommence ; les traits du diagramme et le cercle guide sont `aria-hidden`, les points sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime l'apparition progressive des traits.

Voix : Des notes de laboratoire en sentence case : « Trace the five points in order », « The figure is closed », « Begin again at the first point », « Read the inscription », « Close the notebook ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de présenter le pentacle comme un sigil du canon — c'est un diagramme de travail original, jamais un symbole officiel recopié, jamais un logo. Refuse l'extrait lisible d'emblée, la marge remplie d'inventions, les noms d'entités fabriqués, les titres d'Arcane non vérifiés, le dégradé généralisé, les particules et les cartes arrondies identiques. Refuse de séparer le sceau `EV-0001-001` de sa référence : le gloss reste caché tant que la figure n'est pas fermée.
