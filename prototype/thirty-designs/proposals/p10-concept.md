# The Lantern Archive

Tagline : The page keeps its sentence in the dark until you bring the light near enough to read it.

Palette : Charbon `#141210` (papier sombre, marge, ombre) ; Oxblood `#692129` (tache de cire rouge, sceau) ; Or `#CBA64E` (flamme, halo, masque de lecture, focus) ; Parchemin `#E8DBBD` (lettres révélées, gloss littéral, libellés).

Typographie : Cormorant roman porte la marque, le titre et la référence `Volume 1, chapter 1 — Crimson` en italique, seul usage de l'italique ; c'est la voix de la lampe posée sur la page. Spectral 400 porte l'extrait masqué et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, `@font-face` local, aucune police distante.

Layout : Une grande feuille sombre, sans décor, où l'extrait n'existe que sous la flaque de lumière que l'utilisateur déplace ; la flamme, la tache de cire et le masque de lecture forment le seul geste fort. En-tête discret, gloss et retour en bande basse.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Lantern Archive                                │
│  ┌──────────────────────────────────────────┐      │
│  │   · · ·  ◇ lumière  · · ·  ▪ cire  · ·   │      │  ← flaque (geste)
│  │   « A gaudy and dazzling dreamworld …»   │      │
│  └──────────────────────────────────────────┘      │
│        Move the lantern over the red mark          │
│  [ Read the inscription EV-0001-001 ]               │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur déplace la flamme sur la feuille (glisser au pointeur, flèches au clavier) ; le texte n'apparaît que dans le cercle de lumière, et lorsqu'il pose la flamme sur la tache de cire oxblood la lecture se verrouille et l'extrait reste ouvert. Il presse alors « Read the inscription » avec le sceau `EV-0001-001` pour lire le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, puis « Lower the lantern » éteint la flamme et referme tout ; halo, flamme et cire sont `aria-hidden`, la feuille est une cible tactile de 44 px avec un focus doré, et `prefers-reduced-motion` supprime le fondu du halo.

Voix : Des gestes de lecture en sentence case, sans emphase : « Move the lantern over the red mark », « The mark is lit », « Read the inscription », « Lower the lantern ». Pas de majuscules décoratives, pas de séparateur « A · B · C », pas de flèches collées au libellé.

Refus : Refuse d'éclairer toute la page — la lumière reste locale et fonctionnelle, jamais un dégradé décoratif généralisé, jamais de particules, jamais de fond clair ni de nébuleuse photo. Refuse l'extrait lisible par défaut, les cartes arrondies identiques, les noms d'entités fabriqués, les titres d'Arcane non vérifiés et tout fait ajouté au chapitre un. Refuse de séparer le sceau `EV-0001-001` de sa référence : le gloss reste caché tant que la flamme n'a pas trouvé la cire.
