# Cathedral of the Gray Fog

Tagline : Light the single candle and the fog lifts just enough to read what the glass remembers.

Palette : Charbon `#14110F` (pierre de la nef, fond, ombre des colonnes) ; Oxblood `#4A1520` (verre profond des vitraux, draperies, cire du cierge) ; Or `#C8A24C` (filets de plomb, halos, flamme, anneau de focus) ; Parchemin `#E4D7B6` (extrait, gloss littéral, libellés). La « brume grise » n'est pas une cinquième couleur : un voile de parchemin à faible opacité posé sur le charbon, qui s'éclaircit seulement là où porte la flamme.

Typographie : Cormorant porte la voix « liturgique » — roman pour les noms d'entités et les chiffres de volume gravés dans la pierre, italic réservé à l'inscription du vitrail et au mot « Fog » (seul usage de l'italique, pas une troisième famille). Spectral 400 porte le corps, l'extrait et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, toutes deux chargées via `@font-face` depuis les fichiers locaux (`cormorant-roman`, `cormorant-italic`, `spectral-400`, `spectral-500`), aucune police distante.

Layout : Une nef verticale occupe toute la hauteur et constitue l'unique geste fort — en-tête discret en haut, bande d'extrait et sceau de preuve en bas, le tout calme. Les colonnes et les vitraux de sigils sont dessinés en traits fins et en panneaux CSS (aucun dégradé décoratif, aucun bitmap) ; la lumière du cierge est le seul point lumineux de la page et ne révèle qu'un vitrail à la fois, l'extrait restant voilé sous la brume jusqu'à l'allumage.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                 Volume one    │  ← marque + repère
├────────────────────────────────────────────────────┤
│   │  ▣  │   │  ▣  │   │  ▣  │   │  ▣  │             │  ← vitraux de sigils
│   │     │   │     │   │ ✧   │   │     │             │
│   │  ▣  │   │  ▣  │   │[▣]  │   │  ▣  │             │  ← vitrail révélé
│   │     │   │     │   │     │   │     │             │
│   ═══════════ allée centrale (nef) ═══════════      │
│                    ♨  cierge                        │  ← geste (source unique)
│   « A gaudy and dazzling dreamworld … shattering. »  │  ← extrait réel (voilé)
│      [ sceau EV-0001-001 ]  ‹ Return to the nave     │  ← preuve + retour
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur allume l'unique cierge au pied de la nef (clic ou Entrée) — la flamme monte, écarte localement le voile de brume et fait luire le vitrail central — puis presse le sceau `EV-0001-001` pour que la lumière transitive perce le verre et révèle, en regard de l'extrait jusqu'ici voilé, le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » avec sa référence `Volume 1, chapter 1 — Crimson`, avant de revenir à la nef par « Return to the nave » qui éteint le cierge et referme la brume ; le cierge est une cible de 44 px, le focus est un halo d'or, les vitraux et colonnes décoratifs sont `aria-hidden`, et `prefers-reduced-motion` supprime le scintillement et la montée animée de la flamme (la révélation devient instantanée).

Voix : Des didascalies de sacristie en sentence case, mesurées et jamais en majuscules — courtes, précises, sans séparateurs « A · B · C » ni flèches collées : « Light the candle », « The fog lifts », « Read the glass », « Return to the nave ».

Refus : Refuse d'être une cathédrale décorative où la brume serait un simple fond — le cierge est la seule source de lumière et le seul chemin d'accès au texte. Refuse les cierges d'ambiance multiples, la nébuleuse photo plein écran, les dégradés généraux, les particules, les cartes arrondies identiques et les vitraux qui s'allumeraient tous en même temps. Refuse d'afficher l'extrait par défaut, d'employer la moindre majuscule dans les libellés, d'inventer un titre d'Arcane, un nom de personnage d'une autre œuvre ou un sigil canonique non vérifié (les vitraux restent des formes géométriques originales), et de séparer le gloss de sa référence : la preuve `EV-0001-001` reste solidaire du vitrail « Crimson », illisible sans que le cierge n'ait d'abord été allumé.
