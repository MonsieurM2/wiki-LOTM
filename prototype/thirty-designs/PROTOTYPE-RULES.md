# Règles de création des prototypes

Chaque proposition = **un fichier HTML autonome** `proposals/pNN.html`, CSS et JS inline, écrit depuis son concept `proposals/pNN-concept.md` et le `BRIEF.md`.

## Structure obligatoire

- `<meta charset>` et viewport ; titre « PROTOTYPE pNN — <nom> ».
- `@font-face` pour Cormorant (roman + italic) et Spectral (400/500) avec `src:url('../fonts/....woff2')`.
- Palette et type du concept ; fond sombre ; aucune image bitmap, aucune police distante, aucun appel réseau.
- En-tête avec la marque « Lord of the Mysteries » et un repère de navigation.
- Une zone signature propre au thème : c'est le seul geste audacieux.
- L'extrait du chapitre 1 et la preuve `EV-0001-001` avec sa référence, tels que donnés dans le BRIEF.
- Un moyen d'ouvrir/voir la preuve, et un retour visible.
- Libellés en sentence case, anglais. Pas de MAJUSCULES décoratives, pas de « A · B · C », pas d'em dash entre mot et fragment, pas de flèches collées.
- `.focus-visible` doré, `@media (prefers-reduced-motion: reduce)`, cibles tactiles ≥ 44 px, décoratif en `aria-hidden`.
- Responsive à 820 px.
- JS simple, sans erreur ; moins de ~350 lignes.

## Validation avant de rendre

Vérifie la syntaxe JS en extrayant le `<script>` et en le passant à `node --check` (ou `new vm.Script`). Corrige jusqu'à ce qu'il n'y ait plus d'erreur. Ne crée aucun autre fichier. Retourne uniquement la liste des chemins créés.
