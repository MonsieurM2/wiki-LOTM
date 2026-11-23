# The Patchwork Quilt

Tagline : Pull the loose thread and the seam unravels, parting the fabric to show the sentence sewn beneath.

Palette : Charbon `#171412` (fond, pièces sombres) ; Oxblood `#6E1F27` (couture centrale, fil détendu) ; Or `#C7A24B` (points de couture, focus) ; Parchemin `#E6D7B4` (extrait, glose, pièces claires).

Typographie : Cormorant roman porte la marque et le titre ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Une courtepointe de pièces carrées à points de couture en pointillés, coupée d'une couture centrale oxblood d'où dépasse un fil ; tirer le fil écarte les deux pans et découvre l'extrait. En-tête discret, preuve et retour sous la courtepointe.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Patchwork Quilt                                │
│   ┌───┬───┐│┌───┬───┐                              │
│   ├───┼───┤│├───┼───┤   ← couture oxblood + fil    │
│   └───┴───┘│└───┴───┘                              │
│       « A gaudy and dazzling … »  ← sous le tissu   │
│   [ Read the inscription EV-… ]  [ Resew the seam ] │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur saisit le fil détendu au centre de la couture (clic, Entrée ou Espace) ; les points de la couture s'effacent, les deux pans de tissu s'écartent et l'extrait du chapitre un apparaît coutu dessous. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Resew the seam » referme la courtepointe ; les pièces et la couture sont `aria-hidden`, le fil est une cible de 44 px au focus doré, et `prefers-reduced-motion` supprime l'écartement animé des pans.

Voix : Des indications d'ouvrage en sentence case : « Pull the loose thread », « The seam gives way », « Read the inscription », « Resew the seam ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse les pièces de tissu présentées comme des entités canoniques, les familles de personnages inventées et les titres d'Arcane non vérifiés. Refuse les dégradés décoratifs (chaque pièce est une couleur unie à couture en pointillés), les particules, les cartes arrondies identiques et l'extrait lisible d'emblée. Refuse de séparer le sceau `EV-0001-001` de sa référence : le gloss reste caché sous le tissu jusqu'à l'ouverture de la couture.
