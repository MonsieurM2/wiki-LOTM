# The Sefirah Tree

Tagline : Kindle the lamp at the root and light climbs the branches to the chapter that begins the book.

Palette : Charbon `#141411` (nuit, écorce sombre) ; Oxblood `#71222A` (le nœud du chapitre un, la flamme) ; Or `#CBA64E` (sève lumineuse, lampe, focus) ; Parchemin `#E7D8B5` (extrait, glose, note de marge).

Typographie : Cormorant roman porte la marque, le titre et la note de marge ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Un arbre vivant tracé à traits fins, racine en bas et branches en éventail, avec une lampe à la base et un nœud oxblood pour le chapitre un ; allumer la lampe fait monter la lumière. En-tête discret, extrait dans une marge à droite, preuve et retour en bas.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Sefirah Tree                                   │
│   diagramme original, hors canon                   │
│        ╱╲  ╱╲   ✦                                  │
│       ╱  ╲╱  ●  ← nœud chapitre un                  │
│         │   « A gaudy and dazzling … »  ← extrait   │
│        (lampe) [ Read the inscription EV-… ]        │  ← preuve + retour
│                 [ Let the light fade ]              │
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur allume la lampe à la racine (clic, Entrée ou Espace) ; la sève lumineuse monte le long du tronc et des branches, le nœud oxblood du chapitre un s'allume et l'extrait du chapitre un apparaît dans la marge. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Let the light fade » éteint l'arbre ; le dessin des branches est `aria-hidden`, la lampe est une cible de 44 px au focus doré, et `prefers-reduced-motion` supprime la montée animée de la lumière.

Voix : Des notes de marge en sentence case : « Kindle the root lamp », « The light reaches chapter one », « Read the inscription », « Let the light fade ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de présenter l'arbre ou ses voies comme un diagramme canonique vérifié — c'est un dessin original, jamais une allégation sur le canon ; aucun nom d'entité fabriqué, aucun personnage issu d'autres œuvres de l'auteur, aucun titre d'Arcane non vérifié. Refuse le dégradé décoratif, les particules, les cartes arrondies identiques et l'extrait visible avant d'allumer la lampe. Refuse de séparer le sceau `EV-0001-001` de sa référence.
