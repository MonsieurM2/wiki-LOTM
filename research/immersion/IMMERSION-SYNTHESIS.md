# Immersion maximale du wiki LOTM — synthèse

Question : comment améliorer au maximum l'immersion du site, de façon créative, ludique et ergonomique, sans backend ?

Méthode : **13 sous-agents indépendants**, en trois vagues — 6 lunettes d'idéation (récit, jeu, lecture longue, micro-interactions, architecture de l'information, faisabilité), 4 juges avec un seul critère chacun (fidélité littéraire, anti-gimmick, faisabilité/accessibilité, lecteur de 20 minutes sur portable), 3 synthèses indépendantes (expérience, langage, contrat technique). Aucun juge ne connaissait les autres.

## Résultats des juges

Consensus fort : **T1** recherche Pagefind avec alias et filtres (9 / 9,5 / 7,5) ; **A2** cliquer la phrase pour ouvrir sa preuve (9 / 9) ; **G1** gloses qui se répondent (8 / 8 / 7) ; **E6** citation en regard (8 / 9) ; **E2** glose à la première occurrence (8,5 / 8,5) ; **N2** tirage des 22 Arcanes seedé par date (8 / 9,5).

Consensus moyen : I1 glose au survol **et au focus**, N1 recherche en cartes Tarot, N6 lune colorée, A6 frise des `aliases.until`, I4 fil d'or, E4 lecture une action, E1 ruban, E5 fil de retour, G2 fil des apparitions, G5 échos, A5 fiches oubliées, T5 tiroir par offsets, T7 `stats.json`.

Vetoes convergents :
- **N3 Voile spoiler** — le juge littéraire le note 9,5, mais le juge UX et le juge technique le vetoent : Pagefind indexe le texte nu, donc aucun masquage n'est étanche. Uniquement en **opt-in explicite**, jamais par défaut, jamais présenté comme une garantie.
- **I3 Roue avec inertie et son** — veto unanime (casino, gadget, bruit sur portable).
- **G7 « Ce que le texte ne dit pas encore »** — fabrique du faux canon.
- **T2 Graphe canvas** — remplacé par un graphe SVG par chapitre (A1), accessible.
- **T4 Chronologie virtualisée** — remplacée par une chronologie statique (E1/E8), indexable.
- **T8 Hors-ligne** — reporté.

## Modèle retenu par les synthèses

### Couche 1 — Fondations invisibles

Pagefind avec `canonical_name` + `aliases[].form` indexés et filtres `type/book/status` ; ancrage des phrases par `evidence.offsets` ; `stats.json` dérivé ; grammaire de couleurs unique (or = progression, oxblood = preuve, charbon = corps). Aucune de ces couches n'est visible, toutes sont vérifiables.

### Couche 2 — Signature

| Mécanique | Nom proposé | Geste |
|---|---|---|
| G1 + E2 + I1 | **The Margin / First Naming** | glose oxblood sur la **première occurrence** d'une entité dans un chapitre, ouverte au survol **et au focus**, jamais sur chaque occurrence |
| A2 + T5 + E6 | **The Testimony** | cliquer une phrase ancrée ouvre sa citation littérale en regard, chapitre et livre ; la preuve, pas un résumé |
| N2 + N1 + N6 | **The Drawing** | 22 Arcanes seedés par date UTC, tirage identique pour tous les visiteurs d'un jour ; lune colorée ; résultats en cartes avec repli liste |

### Couche 3 — Optionnel et périphérie

Échos de formulation (G5), frise des `aliases.until` (A6), fiches de degré 1 « The Forgotten » (A5), fil des apparitions (G2), ruban de chapitres (E1), fil de retour (E5), lecture une action (E4), graphe SVG par chapitre (A1). **The Fog** (N3) reste hors défaut.

## Contrat technique

- Aucun fichier lourd téléchargé au runtime. `entity-index` et `edges` servent uniquement au build ; les îlots reçoivent des props.
- 4 îlots React : recherche, tiroir de preuve, rituel seedé par date, voile optionnel. Tout le reste reste HTML statique, indexable, navigable sans JS.
- Règles de dérivation : première occurrence = `min(evidence.chapter)` puis `min(offsets[0])` ; alias actif si `until` absent ou `chapter ≤ until` ; tirage = PRNG déterministe sur `YYYY-MM-DD` UTC ; aucune ancre sans `evidence.id` existant.
- Cinq tests bloquants : ancrage (`text[a:b] === quote`), intégrité des IDs et inverses, unicité de la première glose, exactitude des alias indexés, 0 arête orpheline + reproductibilité du tirage.

## Risques identifiés

- **Taille GitHub Pages** : ~26 500 pages HTML × ~50 Ko ≈ **1,3 Go**, au-delà du plafond recommandé de 1 Go. À arbitrer dans la Stack technique (regroupement des fiches par type avec ancres, ou réduction du HTML par fiche).
- `aliases.until` et la densité réelle des relations n'ont pas été mesurés sur les 1394 chapitres : plusieurs mécaniques (A6, A5, G5) dépendent de leur remplissage réel.
- Le tirage seedé par date paraîtra arbitraire si le visiteur change d'horloge : le cadrer dans la phrase d'interface.

Branche jetable, jamais mergée. Les décisions finales appartiennent à l'humain et sont enregistrées dans le ticket.
