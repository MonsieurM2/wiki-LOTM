# Enrichissement visuel — plan de design

## Sujet, public, travail

Sujet : Lord of the Mysteries, 1394 chapitres, une mythologie victorienne occulte. Public : des lecteurs qui connaissent l'œuvre et vont passer des heures ici. Travail : lire, vérifier chaque affirmation, errer — avec un sentiment d'entrer dans un manuscrit, pas de consulter une base.

Le trait le plus caractéristique reste la **glose en marge** décidée plus haut. L'image ne doit pas la concurrencer : elle doit installer le climat en haut de page, puis s'effacer.

## Ce que les références apportent — et ce qu'on ne copie pas

- Wiki officiel (capture fournie) : nébuleuse photo plein fond, calligraphie chinoise, ornements baroques, carrousel. On garde l'**ambition atmosphérique**, on rejette le fond photo plein écran et le logo calligraphique.
- lotmcompanion : noir violacé, dessin au trait d'un personnage, symboles alchimiques en filigrane, retenue extrême. On garde les **glyphes alchimiques**, on rejette le grand portrait central (et tout visage de personnage, non vérifiable).
- lomworld : noir absolu, un unique pendant doré suspendu, rien d'autre. On garde l'**objet unique et lumineux**, on rejette le centrage vide et le « ganglion » ochre qui dirige tout le regard.
- unofficial.vercel.app : inaccessible lors de l'analyse — aucune inspiration tirée.

## Tokens

Couleur (inchangés) : `ink #070605`, `vellum #e9e1d0`, `gold #b9952f`, `oxblood #6d1f2b`, `ash #9a9080`, `veil #14100d`.
Typographie (inchangée) : Cormorant Garamond (titres, noms), Spectral (corps, interface), auto-hébergées.
Image : une seule, en bandeau de 150 px, gravure cuivre + lavis d'encre, lune écarlate, astrolabe, cartes, brume ; fondu vers l'encre en bas (`mask-image`) pour que le texte reste dominant. `aria-hidden`, aucune information portée par l'image.
Marque : sigil géométrique original (croissant + œil + spirale), traits or fins, ni lettres ni calligraphie — distinct du logo officiel, aucun droit d'auteur repris.

## Principes

1. Une seule audace : le bandeau. Tout le reste reste calme.
2. Aucune image par fiche ; les preuves restent des citations, pas des illustrations.
3. L'image est décorative et masquée aux lecteurs d'écran ; elle ne remplace aucun contenu vérifié.
4. Pas de fond plein écran, pas de dégradé décoratif ailleurs, pas de particules.
5. La marque ne reprend ni le logo officiel ni les ornements du wiki fan.

## Revue avant exécution

Les défauts génériques repérés et écartés : fond nébuleuse plein écran (copie du wiki officiel), portrait central au trait (copie de companion), objet suspendu unique centré (copie de lomworld), browns/terracotta, cartes arrondies, ALL-CAPS eyebrows, `A · B · C`, flèches ajoutées partout. Le bandeau gravé découpé est un choix spécifique à ce sujet : c'est une **planche d'illustration de manuscrit**, pas un fond.

## Critère de réussite

Un visiteur reconnaît LOTM en moins de deux secondes, puis oublie l'image pour lire — et aucune affirmation affichée n'est inventée.

## Critique après exécution

Deux juges indépendants ont noté la première version 6/10 (facture graphique) et 7/10 (distance aux références). Leurs défauts convergeraient :

- l'astrolabe était un diagramme de compas trop parfait → centres décalés de 1–2 px, hachures à faible opacité, graduations irrégulières ;
- les trois cartes étaient le même primitive répété → trois motifs distincts (œil, clé, spirale) et ornements de coin ;
- les six glyphes `☿ ♄ ♃ ☽ ☉ ♀` étaient des caractères unicode empruntés au vocabulaire de lotmcompanion → remplacés par trois sceaux géométriques originaux ;
- le disque rouge rayé ressemblait à un globe filaire et restait trop proche de l'emblème canonique → croissant éclaté désaturé, halo réduit, motifs secondaires à poids égal ;
- le sigil trop « médaillon ésotérique générique » → croissant asymétrique seul, accent oxblood ;
- le bandeau recadrait mal les pages courtes → hauteur 130 px et `viewBox` adapté, astrolabe et cartes conservés.

**Génération bitmap indisponible** : deux requêtes de génération d'images ont échoué pour solde de crédits insuffisant. Aucune n'a été relancée. Le graphique livré est entièrement vectoriel, dessiné à la main — ce qui est aussi plus léger et net à toute taille.

Contrôle final : trois vues capturées, zéro erreur console, bandeau masqué et `aria-hidden`, `prefers-reduced-motion` respecté.
