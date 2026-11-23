# The Reliquary

Tagline : Break the wax seal on the case and the chapter fragment is finally visible under glass.

Palette : Charbon `#151412` (salle des reliques) ; Oxblood `#7A2429` (cire, doublure du socle) ; Or `#CBA649` (monture de la vitrine, focus) ; Parchemin `#E8D9B6` (extrait, étiquette, glose).

Typographie : Cormorant roman porte la marque, le titre et l'en-tête de l'étiquette ; son italique porte la référence `Volume 1, chapter 1 — Crimson`, seul usage de l'italique. Spectral 400 porte l'extrait dans la vitrine et le gloss littéral ; Spectral 500 porte les commandes et le repère de navigation. Deux familles seulement, via `@font-face` local, aucune police distante.

Layout : Une vitrine au centre, vitre scellée d'un disque de cire, socle en dessous ; lever le couvercle découvre l'extrait, puis une étiquette se déplie sous le socle. En-tête discret, preuve et retour sous l'étiquette.

```
┌────────────────────────────────────────────────────┐
│ Lord of the Mysteries                  Volume one   │  ← marque + repère
├────────────────────────────────────────────────────┤
│ The Reliquary                                      │
│      ┌────────────────────┐                        │
│      │        ●           │  ← sceau de cire        │
│      │  « A gaudy and … » │  ← extrait sous vitre   │
│      └────────────────────┘                        │
│      [ Break the seal ]  [ Read the label EV-… ]    │  ← preuve + retour
│      ┌ - - - - - - - - - ┐  ← étiquette détachée    │
│      │ The sound asleep …│                         │
└────────────────────────────────────────────────────┘
```

Geste signature : L'utilisateur brise le sceau de cire (clic, Entrée ou Espace) ; le couvercle se soulève et l'extrait du chapitre un devient lisible dans la vitrine, puis « Read the label » avec le sceau `EV-0001-001` déplie une étiquette portant le gloss littéral « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » et sa référence `Volume 1, chapter 1 — Crimson`, et « Reseal the case » referme tout ; la vitre, le sceau et le socle sont `aria-hidden`, les commandes sont des cibles de 44 px au focus doré, et `prefers-reduced-motion` supprime le soulèvement animé.

Voix : Des cartels de musée en sentence case : « Break the seal », « The fragment is visible », « Read the label », « Reseal the case ». Aucune majuscule décorative, aucun séparateur « A · B · C », aucune flèche collée.

Refus : Refuse de présenter l'objet comme une relique canonique authentifiée ou d'inventer une provenance, un nom d'entité ou un titulaire ; le dessin est original et purement décoratif. Refuse le fond clair, le dégradé décoratif, les particules, les cartes arrondies identiques et un extrait visible avant la levée du sceau. Refuse de séparer le sceau `EV-0001-001` de sa référence.
