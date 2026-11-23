# The Folio of Echoes

Tagline : Repeat the line until one phrase stays sharp and every other copy sinks out of sight.

Palette : Charbon `#141315` (fond et brume) ; Oxblood `#7C242C` (le filet sous l'extrait, le sceau de la preuve) ; Or `#CBA548` (l'écho qui reste net, le focus) ; Parchemin `#E8D9B7` (l'extrait et le gloss littéral).

Typographie : Cormorant roman porte la marque et le titre, son italique porte l'écho net et, seule, la référence `Volume 1, chapter 1 — Crimson` ; Spectral 400 porte l'extrait et le gloss littéral ; Spectral 500 porte l'indice et les commandes. Deux familles, quatre fichiers locaux, aucune police distante.

Layout : Une seule colonne sur fond nu : l'extrait est posé une fois, puis chaque geste empile une copie plus floue et plus pâle de sa première phrase, jusqu'à ce qu'une ligne nette émerge et que la preuve soit consultable.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Folio of Echoes                                │
│                                                    │
│  « A gaudy and dazzling dreamworld … »             │  ← extrait
│    a gaudy and dazzling dreamworld …               │  ← échos qui
│      a gaudy and dazzling dreamworld …             │    s'enfoncent
│        a gaudy and dazzling dreamworld …           │    dans la brume
│   ─── a gaudy and dazzling dreamworld … ───        │  ← écho net (or)
│                                                    │
│      [ Cast another echo ] [ Let it close ]        │  ← geste + retour
│  [ Read the source line EV-0001-001 ]              │  ← preuve
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur lance un écho (Entrée ou Espace au clavier) ; une copie de la première phrase s'enfonce un peu plus dans la brume à chaque fois, et au troisième écho une ligne nette apparaît en or, puis « Read the source line » avec le sceau `EV-0001-001` donne le gloss « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Let the fog close » efface les échos ; les copies qui se dissipent sont `aria-hidden`, les commandes sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime le glissement animé des échos.

Voix : Des consignes feutrées en sentence case : « Cast another echo », « Two echoes remain », « One line stays sharp », « Read the source line », « Let the fog close ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de multiplier un texte inventé : chaque copie répète à l'identique la première phrase de l'extrait, et les échos ne sont pas des voix canoniques. Refuse le fond clair, le dégradé brumeux généralisé, les particules, les cartes arrondies et les bordures décoratives superflues. Refuse de séparer le sceau `EV-0001-001` de sa référence.
