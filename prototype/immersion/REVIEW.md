# Procès-verbal de jugement — démo d'immersion

Trois juges indépendants ont examiné la première version de la démo (fichier + quatre captures), sans concertation.

| Juge | Note | Verdict court |
|---|---|---|
| Fidélité littéraire | 5/10 | Direction graphique juste, mais codes de Tarot inventés et « prophéties » fabriquées |
| Accessibilité / ergonomie | 5/10 | Deux gestes signature inopérants au clavier, focus perdu à chaque écran |
| Lecteur de 20 minutes | 6,5/10 | Le fil doré est le « oh », mais la recherche ne réagit pas et « Continuer » mentait |

## Corrections appliquées

**Fidélité**
- Purge des codes de Tarot non vérifiés : ne subsistent que les noms et alias attestés par le texte et l'audit (Klein, Sharron/Sharon, Shermane/Sherman, Mr. Fool/Mr Fool, Audrey, Emlyn, Cattleya, Alger). Suppression des décomptes de mentions et des titres d'Arcanes inventés.
- Lune écarlate pleine à la place du croissant doré ; plus de seed technique affiché ; libellé « Only the archive. No prediction. »
- L'écho pointe désormais vers une vérité de l'audit (`Sharon` → `Sharron` au tome 2) et ouvre la recherche sur ce nom.

**Accessibilité**
- `.proofable` focalisable (`tabindex`, `role=button`), focus déplacé vers la fermeture du tiroir puis restitué.
- Indicateur de focus du champ de recherche restauré (outline doré), cibles tactiles ≥ 44 px.
- Navigation avec `aria-current` et focus restauré sur le bouton actif ; libellé du voile dynamique avec `aria-pressed`.
- Le fil vers la glose se déclenche aussi au clic, pas seulement au survol.

**Plaisir immédiat**
- Le champ de recherche filtre réellement les noms, résout les alias et affiche un état vide ; les cartes mènent au chapitre.
- « Continuer » ouvre un vrai chapitre 2 (extrait source) avec retour au chapitre 1.
- Favicon, suppression du 404, captures de contrôle : 4/4 écrans, zéro erreur console, tirage reproductible à date égale.

Le jugement n'a pas été rejoué après correction : c'est une passe de plus, pas une preuve de qualité définitive.
