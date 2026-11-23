# Case Files — Bureau of Mysteries (version finale, révision 2)

**Réf. BM-07/B · Objet : habillage du wiki, organisation inchangée · Classification : ouvert.**

## Le principe

Le site est un **dossier d'enquête physique** : papier kraft, machine à écrire, cachets rouges, tampon fantôme, sommaire à onglets numérotés, fiches de preuve encadrées. C'est le langage visuel du Tarot Club — on y reçoit des demandes, on confronte des témoignages, on classe des pièces. La métaphore est canonique et doit se *voir*.

## Ce qui s'est passé entre les deux révisions

La révision 1 avait « approfondi » le concept en le sage-fié : serif pour tout, monospace réduit aux identifiants, cachet réduit à 34 px, kraft désaturé. Le résultat était propre mais avait **perdu le réalisme du dossier**, qui est précisément ce que tu avais choisi. La révision 2 restaure le langage de la proposition 07 et ne corrige que ses vrais défauts.

## Ce qui a été corrigé (et rien d'autre)

1. **Étiquette anglaise** : `RÉF·` (français) devient `REF.` dans la bande des fiches de preuve. Le site est anglais.
2. **Lisibilité des métadonnées** : manille `#C9BC9C` → `#DCCFB0`, numéros de référence `#8A7E60` → `#A89A7A`, cachet `#9A342A` → `#B04338`. Le grain kraft et le tampon restent, mais les petits textes se lisent.
3. Tout le reste est conservé : papier kraft texturé, grand cachet circulaire en filigrane, typographie typewriter en capitales espacées, sommaire `01 / CHAPTER` avec tampon incliné sur l'onglet actif, `CHAPTER 1: CRIMSON` souligné en pointillé, panneau de marge à double cadre, fiches à filet rouge, perforation sur « Continue reading ».

## Tokens

- `kraft #3A342B` — fond, papier d'archive
- `encre #141210` — panneaux et sommaire
- `paper #DCCFB0` — texte
- `cachet #B04338` — tampons, filets d'autorité, onglet actif
- `ref #A89A7A` — numéros et métadonnées

Typographie : monospace à chiffres tabulaires pour tout l'interface, italique pour les citations. C'est un choix lié au sujet — la machine à écrire du dossier — pas un défaut générique.

## Limite assumée

Le grain et le grand filigrane coûtent un peu de contraste. Ils sont volontaires : c'est le prix du réalisme. La correction s'est limitée à éclaircir les textes pour que la lecture de 1394 chapitres reste possible.

## Version définitive

**`PROTOTYPE-FINAL.html` est la version retenue** — voir `screenshot.png` après remplacement. Elle ajoute à la révision 2 deux derniers éléments de cohérence, sans rien retirer au réalisme :

1. une **tranche rouge** court sur le bord gauche de la feuille : le dossier a un dos, pas seulement une couleur de fond ;
2. la mention de volume devient une **classification entre crochets** `[ VOLUME 1, CLOWN ]`.

`PROTOTYPE.html` (révision 1, trop sage) et `PROTOTYPE-v2.html` (révision 2) restent dans le dossier comme traces du chemin parcouru — aucune n'est à utiliser.

Cette version est gelée. Toute modification future sera une nouvelle décision, pas un raffinement implicite.
