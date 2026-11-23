# Orchestration du corpus

Un seul manifest, `data/manifest.json`, porte l'état des chapitres 1–1394 :
`pending` (à faire), `in_progress` (en cours), `done` (fait), `dispute`
(désaccord non tranché). Les chapitres sont regroupés en lots de 50. Un seul
processus écrit le manifest : l'orchestrateur réclame les chapitres et les
distribue aux sous-agents, qui ne le modifient jamais.

## Procédure

1. Initialisation, une seule fois : `python orchestration/manifest.py init`.
2. Une session de travail : `next --agent <id>` rend `{chapter, batch}`. Le
   chapitre passe en `in_progress`. Le sous-agent produit
   `data/chapters/C####.json`, que `schema/validate.py` doit valider.
3. Succès : `complete <n>` — refuse de marquer `done` si le JSON généré manque.
4. Désaccord : `journal <n> <fact_id> CORRECT|DISPUTE|MISSING` avec les champs
   `before`, `after`, `reason`, `verifier`, puis `dispute <n>` si le fait reste
   en attente. Le journal `data/disagreements.jsonl` est append-only et chaque
   entrée est dédupliquée par `(chapter, fact_id, kind)`.
5. Reprise après crash : `recover` remet tous les `in_progress` en `pending` ;
   `next` rend alors exactement le premier chapitre non fait du lot courant.
   Les tentatives sont conservées pour le suivi de coût.
6. Contrôle : `status` donne les compteurs, le lot courant et une estimation en
   minutes (11 min de vérification par chapitre, mesurées dans le prototype).

Plusieurs sessions peuvent travailler en parallèle en réclamant des lots
différents : `next --agent <id> --batch <n>`.

Vérification : `python orchestration/test_manifest.py` — simule un crash en
plein lot puis vérifie la reprise, l'interdiction de marquer `done` sans donnée,
le gel des désaccords et l'absence de doublon dans le journal.
