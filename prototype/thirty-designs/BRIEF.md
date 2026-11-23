# Cahier des charges commun — 30 propositions

## Projet

Wiki anglais sur **Lord of the Mysteries** (LOTM), 1394 chapitres, une fiche par entité nommée (8 types fermés), chaque fait portant une preuve : livre + chapitre + citation anglaise littérale. Static Astro + React + Pagefind + GitHub Pages, aucun serveur.

## Contraintes dures (aucune proposition ne peut les violer)

1. Anglais pour tout le contenu visible.
2. Charbon, oxblood, or, parchemin ; jamais de fond clair, jamais de nébuleuse photo plein écran.
3. Une seule famille serif pour les titres/noms et une pour le corps/interface ; utiliser les polices locales fournies (`../fonts/cormorant-roman.woff2`, `cormorant-italic`, `spectral-400`, `spectral-500`) via `@font-face`. Aucune police distante.
4. Une seule chose audacieuse par écran ; tout le reste calme. Pas de dégradé décoratif généralisé, pas de particules, pas de cartes arrondies toutes identiques.
5. Anglais, sentence case : pas de libellés en MAJUSCULES, pas de chaînes « A · B · C », pas d'eyebrows superflus, pas de flèches collées partout.
6. Preuve = glose/citation littérale avec référence `Volume 1, chapter 1`. Aucune affirmation inventée, aucun nom de personnage issues d'autres œuvres de l'auteur, aucun titre d'Arcane non vérifié.
7. Accessibilité : focus clavier visible, `prefers-reduced-motion`, cibles tactiles ≥ 44 px, éléments décoratifs `aria-hidden`.
8. Un seul fichier HTML autonome par proposition, sans dépendance externe ni image bitmap. Aucun appel réseau. Aucun logo officiel recopié.

## Ce qui doit apparaître dans chaque prototype

- Un en-tête avec la marque « Lord of the Mysteries » et un repère de navigation.
- Une zone signature propre au thème, qui est le seul geste fort de la page.
- Un extrait de chapitre réel : « A gaudy and dazzling dreamworld filled with murmurs instantly shattered. The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head as though someone had ruthlessly lashed at him with a pole again and again. »
- Une preuve associée : `EV-0001-001` — « The sound asleep Zhou Mingrui felt an abnormal throbbing pain in his head » — `Volume 1, chapter 1 — Crimson`.
- Un moyen d'ouvrir/voir cette preuve, et un retour visible.

## Format du concept (fichier `pNN-concept.md`)

```
# <nom de la proposition>
Tagline : <une phrase, en anglais>
Palette : <4 hex nommés>
Typographie : <rôles des deux familles>
Layout : <une phrase + petit wireframe ASCII>
Geste signature : <ce que l'utilisateur fait, une phrase>
Voix : <une phrase sur le ton des libellés>
Refus : <ce que cette proposition refuse explicitement>
```

## Format du prototype (fichier `pNN.html`)

Un seul fichier HTML complet, CSS et JS inline. Doit s'ouvrir par double-clic et aussi via le serveur local. Aucun texte généré par IA visible dans l'interface. Reste sous ~350 lignes. Retourne uniquement le chemin du fichier.
