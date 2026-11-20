# Verdict du prototype — pipeline extraction / vérification

**Question** : le modèle « extracteur → vérificateur indépendant → arbitrage » tient-il les cas limites sans laisser entrer de fait non vérifié, et à quel coût ?

**Réponse** : oui, à condition que le vérificateur **complète** l'extraction au lieu de seulement la confirmer. Sur 3 chapitres réels, 63 preuves : 52 confirmées telles quelles, 11 réparables par ancrage ou libellé, 0 contradiction de fait — mais 24 faits évidents manqués.

## Mesures

| Chapitre | Evidence | Confirm | Correct | Dispute | Faits manqués | Temps vérif. |
|---|---:|---:|---:|---:|---:|---:|
| 1 — Crimson | 11 | 11 | 0 | 0 | 6 | ~12 min |
| 2 — Situation | 22 | 18 | 4 | 0 | 8 | ~10 min |
| 3 — Melissa | 30 | 23 | 7 | 0 | 10 | ~12 min |
| **Total** | **63** | **52** | **11** | **0** | **24** | ~34 min |

~11 min de vérification par chapitre → ~255 heures d'agent pour 1394 chapitres.

## Décisions

- `CONFIRM` entre tel quel ; `CORRECT` entre avec la réparation du vérificateur (ancrage ou libellé), sans humain ; `DISPUTE` (contradiction sur le texte) est mis en attente d'arbitrage humain ; non résolu = exclu.
- Le vérificateur **produit** les faits manqués avec citations : la sortie de l'extracteur est un brouillon.
- Journal append-only `data/disagreements.jsonl`, une entrée par `CORRECT` / `DISPUTE` / `MISSING` : `{chapter, fact_id, kind, before, after, reason, verifier, timestamp}`. Non public.
- Trou révélé dans le schéma : les types d'entités n'étaient pas déclarés → `entities[]` ajouté à `schema/chapter.schema.json` et à l'exemple du chapitre 1 sur `main`.
- Vérification intégrale conservée ; le suivi de coût et la reprise incombent à l'orchestration.

## Assets

- `PROTOTYPE-WIPE-ME-arbitration.html` — démo autonome, 4 scénarios, machine à états pure vérifiée en Node (4/4).
- `out/extractor-chapter-000{1,2,3}.json` — extractions brutes.
- `out/verifier-chapter-000{1,2,3}.json` — verdicts indépendants (réouverts depuis l'epub).
- `PROTOTYPE-WIPE-ME-measure.py` — agrégation des mesures.

Branche jetable, jamais mergée.
