# Case Files — Bureau of Mysteries (version finale)

**Réf. BM-07/B rev.2 · Objet : habillage du wiki, organisation inchangée · Classification : ouvert.**

## Le principe

Le site n'est pas un déguisement de détective. C'est un **dossier bien tenu** : chaque chapitre est un rapport, chaque fiche une personne identifiée, chaque citation une pièce versée au dossier avec sa référence. Le lecteur n'a rien à résoudre — il lui suffit de pouvoir vérifier, et de retrouver son chemin. C'est exactement le fonctionnement du Tarot Club dans l'œuvre : on y reçoit des demandes, on y confronte des témoignages, on y rend des comptes. La métaphore est canonique ; elle n'a pas besoin d'être soulignée.

Ce qui a été refusé de la version 07 : le monospace appliqué à tout le texte, les majuscules généralisées, le cachet géant en filigrane fixe, la grille papier-bruitée sur toute la page, l'étiquette française injectée en CSS. Tout cela faisait « accessoire de costume » et fragilisait la lecture de 1394 chapitres.

## Tokens

- `ink #0e0d0b` — fond, noir de chemise de classement
- `file #24201a` — kraft désaturé des panneaux
- `paper #ded3bb` — texte, parchemin d'archive
- `oxblood #6d2027` — seule marque d'autorité : référence de preuve, onglet actif
- `graphite #948a78` — métadonnées, numéros, filets

Typographie — deux rôles, pas deux décorations :
- **Cormorant Garamond** : titres et noms propres (la voix humaine de l'archive)
- **Spectral** : corps et interface (la lecture longue)
- **monospace système** : uniquement les identifiants `EV-0001-001` et les numéros de référence. Jamais une phrase.

## Règles de mise en page

1. La chemise se lit en haut : un filet fin, un onglet d'en-tête avec `Ref. BM-07/B`, aucun tampon géant.
2. Les gloses marginales deviennent des **fiches versées au dossier** : fond kraft, filet oxblood à gauche, référence en monospace, citation en serif italique.
3. Le sommaire est un **index de classeur** : numéros tabulaires, casse normale, l'onglet actif marqué d'un simple filet oxblood — pas de tampon incliné.
4. La citation prouvée porte un petit sceau texte `verified` en oxblood, pas un cachet graphique.
5. Le grain papier reste aux bords (filets, ombres), jamais au-dessus du texte.

## Équilibre

Une seule chose frappe : la **discipline typographique** — serif pour lire, monospace pour vérifier. Le reste est calme. C'est ce qui rend le concept « dossier » crédible sans devenir exotique.

## Risque

L'oxblood sur kraft reste le point sensible : réservé aux filets et aux références, jamais au corps du texte, il doit être vérifié en contraste réel. Le monospace, limité aux identifiants, évite la fatigue de lecture de la version 07.
