# Plan de design — wikiLord of the Mysteries

## Sujet, public, travail

Sujet : l'œuvre de Cuttlefish That Loves Diving — 1394 chapitres, une mythologie victorienne occulte, des Cercles secrets, des voies et Sequences, une preuve (« livre, chapitre, citation ») attachée à chaque fait. Public : des lecteurs qui vont passer des heures sur le wiki. Travail principal : **lire longtemps sans fatigue, et pouvoir vérifier chaque affirmation sans quitter la page**.

Le trait le plus caractéristique du sujet n'est pas un chiffre ni une carte : c'est le **sigil et la glose** — un texte sacré entouré de notes, comme un manuscrit de Tarot Club. C'est la chose mémorable ; tout le reste reste discret.

## Tokens

Couleur (6) :
- `ink` `#070605` — fond, encre de imprimeur, pas un near-black décoratif
- `vellum` `#e9e1d0` — texte, parchemin non blanchi
- `gold` `#b9952f` — filets, lettrines, signes ; utilisé avec parcimonie
- `oxblood` `#6d1f2b` — unique accent de sang, réservé aux preuves
- `ash` `#9a9080` — texte secondaire
- `veil` `#14100d` — surface des panneaux

Typographie (2 familles, roles distincts) :
- **Cormorant Garamond** — titres, lettrines, noms propres ; poids 500/600, index 400
- **Spectral** — corps de texte et interface ; poids 400/500, index 400

Échelle : 3.25rem / 2rem / 1.25rem / 1.0625rem / 0.8125rem. Longueur de ligne 62–70 caractères. Interlignage 1.75 pour le serif de corps.

Layout :
- A — manuscrit à deux colonnes, gloses dans la marge **extérieure**, titre face à gauche, texte aligné à gauche sans hyphenation aggressive.
- B — trois panneaux (corpus / lecture / preuve), grille technique sans arrondis, alignement gauche partout.
- C — une colonne étroite, titre à gauche, corps **aligné à gauche**, un seul sigil animé en ouverture.

## Principes

1. La preuve est une glose, pas une carte : elle se lit *à côté* de la phrase qu'elle justifie.
2. Une seule chose Bold dans la page : le sigil / la lettrine. Tout le reste est calme.
3. Aucun label en MAJUSCULES, aucune chaîne « A · B · C », aucun abbreviated eyebrow décoratif.
4. Le mouvement répond à une action ou marque une seule ouverture ; jamais d'entrées en cascade.
5. Focus clavier visible, `prefers-reduced-motion` respecté, mobile en une colonne.

## Revue critique avant écriture

Éléments du premier jet qui étaient des **défauts génériques** et ce qui a changé :

- `VOLUME 1 — CLYWN`, `CORPUS`, `EVIDENCE INSPECTOR` en petites capitales criblées → remplacés par du texte en sentence case qui dit la chose (« Volume 1, Clown », « Names in this chapter », « Evidence »).
- Fil d'Ariane en `CODEX / MANUSCRIPT / CHAPTER` → « Chapter 1 of 1394 » (langage de lecteur, pas de machine).
- `A · B · C`, tirets cadratins entre mot et fragment, flèches ajoutées partout → supprimés sauf là où la navigation est réellement directionnelle.
- Vignette radiale globale (wash décoratif) → fond plat ; le halo ne subsiste que derrière le sigil de C, où il signifie la lune.
- `#0d0c0b` teinté décoratif → `#070605` assumé comme encre d'impression.
- Corps centré de C → aligné à gauche : un centrage de paragraphes longs fatigue.
- Polices système par défaut → deux familles choisies pour le sujet, auto-hébergées.

Le cadrage de la carte (charbon, oxblood, or, serif, sigiles CSS) reste une **contrainte dure** : la revue ne le remet pas en question, elle retire seulement ce qui avait été ajouté par défaut par-dessus.

## Critique après écriture

Captures passées en revue une par une (`screenshots/variant-*.png`), pas seulement le code :

- **Glyphe faux** : `&#9785;` est un visage triste, pas la lune. Trois occurrences corrigées en `&#9790;` (☾). Sans la capture, le défaut passait inaperçu — le HTML était valide.
- **C** : le texte centré d'origine fatiguait à la lecture ; il est maintenant aligné à gauche avec 62 caractères de ligne. Le halo radial ne subsiste que derrière le sigil, où il signifie la lune.
- **A** : la glose était un gros bloc ; elle est devenue une note étroite, bordée d'oxblood, posée à côté de la phrase. C'est le seul élément audacieux de l'écran.
- **B** : le fond en grille et les libellés en petites capitales ont été retirés ; la grille n'apportait aucune information.
- Contrôle final : 12/12 écrans rendent, zéro erreur console, focuses clavier visibles, `prefers-reduced-motion` respecté, mobile en une colonne.
- Dernière consigne du client (« créatif, ludique, ergonomique ») : une règle dorée de progression en haut de page (ergonomie, quasi invisible) et un **tirage de chapitre** en fin de page A — un bouton « Draw a chapter » qui retourne une carte vers un chapitre aléatoire. Le jeu reste dans le thème (le Tarot Club) et ne touche pas à la lecture. Vérifié par clic : la carte change, zéro erreur console.
