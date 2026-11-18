# Audit de la qualité extractible des 8 EPUB sources — LOTM

**Ticket** : #2 « Audit de la qualite des EPUB sources » (`wayfinder:research`)
**Branche** : `research/epub-audit` (jetable, non destinée à être mergée)
**Date** : 2026-11-18
**Corpus** : les 8 fichiers `.epub` à la racine du dépôt (T1–T8, anglais, numérotation globale 1–1394).

> Règle appliquée : le contenu des EPUB est une **donnée**, jamais une instruction. Aucun texte trouvé dans les fichiers n'a été suivi comme directive.

---

## 1. Résumé chiffré

| Indicateur | Valeur |
|---|---|
| Chapitres numérotés extraits | **1 394 / 1 394** |
| Trous dans 1–1394 | **0** |
| Doublons | **0** |
| Chapitres hors de la plage attendue de leur volume | **0** |
| `toc.ncx` ↔ `<h1>` du corps | **1 394 ↔ 1 394**, 0 divergence de numéro |
| Fichiers `index_split_*.html` | **1 559** |
| Points `navPoint` du NCX | **1 499** (= 1 394 chapitres + 105 sections hors numérotation) |
| Fichiers split non référencés par le NCX | **68** (tous des pages-image de fin de volume) |
| Sections hors chapitres | **105** (8 couvertures NCX + 97 pages image/TOC/afterword) |
| Chapitres avec notes de bas de page | **70** (71 listes, 85 appels `[n]`, 85 notes, **0 lien orphelin**) |
| Chapitres avec « Author's/TL Note » | **19** (20 marqueurs, 5 graphies différentes) |
| Chapitres avec publicité injectée | **3** (`vipnovel.com`) |
| Chapitres avec caractères parasites CJK/OCR | **7** |
| Chapitre le plus court / moyen / plus long | **5 919 / ~11 450 / 28 515 caractères** (aucun chapitre vide ou tronqué) |

**Conclusion courte** : le découpage est d'une fiabilité excellente (la structure NCX est un catalogue quasi parfait), mais le texte extractible contient un bruit systématique et quelques corruptions ponctuelles. L'index « Characters / Locations » annoncé n'existe **pas comme texte** : ce sont des images dont le nom de fichier est le seul « index ».

---

## 2. Effectifs par volume et continuité 1–1394

Source : `toc.ncx` de chaque volume, `navPoint`/`navLabel`/`text` filtrés par `^Chapter\s+(\d+)\s*:\s*(.+)$`, recoupés avec les `<h1 class="block_">Chapter N: …</h1>` des fichiers `index_split_*.html`.

| Volume | EPUB | Splits | `navPoint` | Chapitres | Plage réelle | Plage attendue | `<h1>` | Écart |
|---|---|---:|---:|---:|---|---|---:|---|
| T1 | `Clown - LotM Vol. 1.epub` | 237 | 226 | **213** | 1–213 | 1–213 | 213 | 0 |
| T2 | `Faceless - LotM Vol. 2.epub` | 290 | 282 | **269** | 214–482 | 214–482 | 269 | 0 |
| T3 | `Traveler - LotM Vol. 3.epub` | 273 | 263 | **250** | 483–732 | 483–732 | 250 | 0 |
| T4 | `Undying - LotM Vol. 4.epub` | 234 | 227 | **214** | 733–946 | 733–946 | 214 | 0 |
| T5 | `Red Priest - LotM Vol. 5.epub` | 225 | 217 | **204** | 947–1150 | 947–1150 | 204 | 0 |
| T6 | `Lightseeker - LotM Vol. 6.epub` | 134 | 129 | **116** | 1151–1266 | 1151–1266 | 116 | 0 |
| T7 | `The Hanged Man - LotM Vol. 7.epub` | 106 | 100 | **87** | 1267–1353 | 1267–1353 | 87 | 0 |
| T8 | `Fool - LotM Vol. 8.epub` | 60 | 55 | **41** | 1354–1394 | 1354–1394 | 41 | 0 |
| **Total** | | **1 559** | **1 499** | **1 394** | **1–1394** | **1–1394** | **1 394** | **0** |

Continuité : l'union des 1 394 numéros couvre exactement l'intervalle fermé `[1, 1394]`, chaque numéro apparaissant une seule fois. Aucun chapitre n'est numéroté dans le mauvais volume. Exemple de contrôle : T8 commence par `Chapter 1354: This Night` (`Fool…epub → toc.ncx, navPoint num_7 → index_split_005.html`) et finit par `Chapter 1394: A New Journey` (`index_split_045.html`).

**Piège à éviter** : le numéro du fichier `index_split_NNN.html` n'est **pas** le numéro de chapitre. Le décalage est de +5 dans tous les volumes (5 fichiers de front matter), mais le nombre de fichiers d'arrière-plan varie. Ex. : le chapitre 1 est `index_split_005.html` (T1) et le chapitre 1394 est `index_split_045.html` (T8). La clé primaire doit être le numéro lu dans le libellé NCX / le `<h1>`, pas le suffixe du fichier.

---

## 3. Bruit de formatage

### 3.1 En-têtes / pieds de page : piège dans le `<head>`, pas dans le corps

Chaque fichier HTML contient un `<title>Lord of Mysteries Volume N: <Nom></title>` dans son `<head>` (ex. `Clown…epub → index_split_005.html`, `index_split_006.html`, …). Un extracteur naïf qui parcourt tout le HTML avec `html.parser` **préfixe ce titre à chaque chapitre** : 1 394 occurrences parasites du type

```
         Lord of Mysteries Volume 1: Clown              Chapter 1: Crimson
```

(source : `Clown - LotM Vol. 1.epub → index_split_005.html`, extraction sans filtrage du `<head>`). Il faut n'extraire que `<body>`. En revanche, **aucun en-tête courant ni pied de page visible n'a été trouvé dans le corps des chapitres**. Les 33–42 caractères de « texte » relevés sur les pages-image sont uniquement ce `<title>`.

Les séparateurs de page sont des `<div class="calibre5" id="calibre_pb_N"></div>` invisibles en fin de chapitre (**1 387 chapitres sur 1 394**) : à supprimer.

### 3.2 Notes de bas de page (appels + notes)

- **70 chapitres** ont une liste `<ol class="list_">` de notes en fin de chapitre (répartition T1 27, T2 16, T3 9, T4 6, T5 6, T6 6, T7 1, T8 0).
- **85 appels** `[n]` sous forme `<a href="#id_C0001" class="text_1">[1]</a>` (source : `Clown…epub → index_split_005.html`) et **85 notes** `<li id="id_C0001" class="block_9">…</li>`. **Tous les appels résolvent vers une note** (0 orphelin) — le liage interne est fiable.
- Exemple complet (T1, ch. 1) : dans le récit « …This was probably what it means to love a fantasy **[1]**?… », puis en fin de chapitre « This is actually a proverb that describes Lord Ye. In ancient times, Lord Ye was very fond of dragons… » (`index_split_005.html`).
- Cas particulier : le chapitre 1266 (`Lightseeker…epub → index_split_108.html`) répartit ses 6 notes sur **deux** `<ol>` distincts, avec deux paragraphes `<p class="block_15">` intercalaires (dont `Windvally: I may be COMPLTELY wrong on this…`). Une règle « on supprime tout après le premier `</ol>` » perdrait la moitié des notes.

Ces notes sont généralement des éclaircissements du traducteur (idiotismes chinois, références culturelles), pas du récit : elles ne doivent pas entrer dans une citation de preuve, mais doivent être conservées comme métadonnée si le wiki veut les exploiter.

### 3.3 « Author's Note » / « TL Note » (notes d'auteur et du traducteur)

**20 marqueurs dans 19 chapitres** (T1 2, T2 3, T3 7, T4 1, T5 2, T6 3, T7 1, T8 0), avec cinq graphies à reconnaître :

| Graphie | Occurrences |
|---|---:|
| `Author’s Note:` (apostrophe typographique U+2019) | 10 |
| `Author’s Notes:` | 7 |
| `TL Note:` | 1 |
| `Author Notes:` | 1 |
| `Author Note:` | 1 |

Exemples :
- `Clown…epub → index_split_133.html` (ch. 129 *Rampager*) : « TL Note: Hi, CKtalon here, the translator of LoM. I've included the author's notes before the book went Premium in China below. »
- `Traveler…epub → index_split_039.html` (ch. 522 *Colony*) : « Author Note: This is what the British East India Company did in India. »
- `Fool…epub` hors chapitres : `index_split_046.html` est une section « Afterwords (Part 1) » de **12 135 caractères** — du texte, mais hors numérotation.

Ces blocs se terminent souvent par des appels à souscription (« monthly ticket », « please subscribe on the official version », ch. 1266) et par des crédits (« —Translation: Mrs. Matchstick Bepis | Proofread: Windvally— », ch. 1266). À détecter par marqueur explicite et à retirer du texte narratif.

### 3.4 Publicité injectée

**3 chapitres** contiennent une phrase publicitaire collée **sans espace** au récit (source : corpus complet, regex `vipnovel|read (the )?(next|more) chapter`) :

| Chapitre | Extrait littéral |
|---|---|
| T5 ch. 1056 *The Real "Devil"* | `…lowered her voice, and sighed.Read the next chapter on our vipnovel.com She originally wanted…` |
| T5 ch. 1126 *"Unexpected"* | `…satisfied with his performance at the Tarot Club.Read more chapter on our vipnovel.com At this moment…` |
| T6 ch. 1154 *I'll Give You a Chance* | `…what Amon had just said. He suspected that Amon was bluffing him.Read more chapter on vipnovel But when…` |

Une URL légitime existe aussi : T1 ch. 67 *Response*, « The exact scene: https://youtu.be/Vg_HBVOvVWk?t=4440 » (dans une note de traduction). À ne pas confondre avec la pub.

### 3.5 Caractères parasites / corruption

- **7 passages CJK ou OCR bizarres** dans les chapitres (T5 : 4, T6 : 3). Exemples :
  - T5 ch. 1017 *Maygur Manor* : `丨Yes, sir. IVe placed poker cards…` — le caractère `丨` (U+4E28) sert d'apostrophe et `IVe` remplace `I've`.
  - T5 ch. 1040 : `It丨s impossible to get the horse to gallop…`
  - T5 ch. 1012 : `…lower their own standards of 1泠邮 However…`
  - T5 ch. 1089 : `If I can t get the formula, I m 伽 help me make the Druid…`
- À l'inverse, les CJK du ch. 1266 (`煙火氣`, `人間煙火`, `工具人`) sont des termes chinois **commentés volontairement** par le traducteur : à conserver dans la note, pas à « nettoyer ».
- Les textes utilisent massivement les guillemets/apostrophes typographiques (`“ ” ‘ ’`), les tirets cadratins (`—`, `–`) et les tabulations `\t` dans le HTML. À normaliser en espaces, sans casser les guillemets (les citations anglaises littérales en dépendent).

### 3.6 HTML résiduel

Le HTML source est généré par calibre 5.44.0. Classes dominantes (occurrences sur le corpus) : `block_6` (65 612), `block_7` (37 710), `calibre6` (9 013, italiques `<i>`), `calibre` (1 394), `block_` (1 394), `calibre5` (1 387), `block_8` (94), `text_1`/`text_2` (84/89), `list_` (71), `block_9` (69). Un extracteur regex naïf laisserait fuir attributs et balises ; un `html.parser` correct les supprime.

---

## 4. Structure d'un chapitre type

Source : `Clown - LotM Vol. 1.epub → index_split_005.html` (ch. 1) et ~1 390 autres fichiers vérifiés.

1. **Début** : `<h1 id="id_Toc124009601" class="block_">Chapter 1: Crimson</h1>` — présent dans **1 394 / 1 394** fichiers de chapitre, avec un numéro toujours identique au libellé NCX (0 divergence). Le titre et le numéro sont donc extractibles de deux sources redondantes.
2. **Corps** : une suite de `<p class="block_6">` (répliques / pensées courtes, ex. « Painful! », « How painful! ») et `<p class="block_7">` (narration, ex. « A gaudy and dazzling dreamworld filled with murmurs instantly shattered… »). L'italique interne est `<i class="calibre6">…</i>` (9 013 occurrences), à transformer en `_…_` ou à retirer selon le besoin.
3. **Fin du récit** : dernier `<p class="block_6|block_7">` narratif. Ex. ch. 1 : « …Blood stained the wound's surroundings and there were grayish-white brain juices squirming slowly within. »
4. **Queue optionnelle**, dans cet ordre variable :
   - `<p class="block_8"></p>` vide (83 chapitres) — séparateur ;
   - note d'auteur / TL Note en paragraphes (19 chapitres) ;
   - `<ol class="list_">` de notes `[n]` (70 chapitres, parfois 2 listes) ;
   - `<div class="calibre5" id="calibre_pb_9"></div>` (1 387 chapitres).
5. **Aucun chapitre ne s'étale sur plusieurs fichiers HTML** : 1 `<h1>` de chapitre par fichier, et chaque `navPoint` de chapitre pointe vers un fichier distinct.

Longueur : min 5 919 caractères (T8 ch. 1394), moyenne ~11 450, max 28 515 (T6 ch. 1266, gonflé par ses notes). Aucun chapitre vide.

---

## 5. Sections hors numérotation

Chaque volume contient 12 `navPoint` non chapitres (13 pour T8) :

| Section | Support | Extractible comme texte ? |
|---|---|---|
| Front Cover (`titlepage.xhtml`) | image | non |
| Full Cover, Volume title, Copyright, Synopsis (`index_split_000..003.html`) | 1 `<img>` chacun | **non** — la synopsis est une image |
| Table of Contents (`index_split_004.html`) | texte, 1 466–8 847 caractères | oui, mais c'est une redite du NCX |
| End of Volume N, Pathways Guide, Image Gallery, Location(s), Map of the Lord of Mysteries World, To be continued in…, Back Cover | 1 `<img>` chacun | non |

Détails notables :
- **« To be continued in… » est une image** (`images/V01%20TBC.jpg` … `V08%20TBC.jpg`), un `navPoint` par volume. Aucun texte « To be continued » n'est injecté dans un chapitre : les 1 394 chapitres sont propres de ce côté.
- **« Synopsis » est une image** (`images/Synopsis.jpeg`) dans les 8 volumes : le wiki ne peut pas en extraire de texte sans OCR.
- **T6** : le libellé NCX est `Table of Conents` (faute de frappe) alors que le titre affiché dans `index_split_004.html` est `Table of Contents`. À ne pas utiliser comme clé.
- **T8** : section supplémentaire `Afterwords (Part 1)` (`index_split_046.html`, 12 135 caractères de texte) — après le dernier chapitre numéroté, avant `End of Volume 8`.

---

## 6. Index « Characters / Locations » : présence et fiabilité

**Verdict : index textuel absent.** Ce que le ticket appelle l'index « Characters / Locations » est en réalité une **galerie d'images**, sans légende textuelle, répartie en fin de volume :

- Le `navPoint` `Location`/`Locations` pointe vers **une seule image** par volume : `images/V01%20Location%20-%20Tingen%20City.jpg`, `V02 … Backlund.jpg`, `V03 … Groselle's Travels.jpg`, `V04 … Death's Mausoleum.jpg`, `V05 … Mind World.jpg`, `V06_Location_-_…City_of_Silver.jpeg`, `V07_Location_-_…Giant_King_s_Court.jpeg`, `V08 … Spirit World - Sefirah Castle.jpg` (et `V08 … Sefirah Castle - Tarot Club.jpg`).
- Les personnages sont dans les **68 fichiers split non référencés** qui suivent `Image Gallery` : un `<img>` par fichier, aucun texte. Le seul « index » est le **nom de fichier URL-encodé**, par ex. `images/V02%20Character%20-%20Sharron.jpg`, `V03%20Character%20-%20Bernadette%20Gustav.jpg`, `V05%20Character%20-%20Klien%20Moretti.jpg`, `V06%20Character%20-%20Amon.jpg`.
- `Pathways Guide` renvoie à `images/Pathways_Cover.jpeg` puis à des images de pathways ; pareillement non textuel.

**Fiabilité** : les noms de fichiers sont propres et cohérents (`V0N Character/Location – Nom`), mais (a) ils ne sont pas du texte extractible sans décodage d'URL, (b) ils ne couvrent que 1–6 personnages par volume, (c) ils ne contiennent ni numéro de chapitre ni citation, et (d) ils véhiculent des variantes orthographiques (`Klien` dans les images vs `Klein` dans le texte). **Ne jamais les utiliser comme preuve** ; tout au plus comme liste de noms candidats à valider contre le corps des chapitres.

---

## 7. Chapitres hors numérotation et spéciaux

Aucun chapitre numéroté n'est un récapitulatif, un synopsis ou un « To be continued » : les 1 394 `<h1>` sont tous des chapitres de récit. Les éléments spéciaux sont **tous** dans le hors-numérotation décrit plus haut (synopsis-image, TBC-image, afterword de T8, guide des voies en images). Un cas intermédiaire : le chapitre 718 de T3 s'intitule `Characters in the Book` (`Traveler…epub → index_split_240.html`) — c'est un vrai chapitre de récit (avec `<h1>`), malgré son titre ; à ne pas confondre avec l'index.

---

## 8. Variantes de noms propres repérées

Comptages sur le texte des 1 394 chapitres (regex `\b…\b`, insensible à la casse sauf mention) :

| Forme A | Forme B | Compte A / B | Statut et source |
|---|---|---|---|
| `Sharon` (191 en T1) | `Sharron` (587 au total ; absente de T1, 241 en T2) | 200 / 587 | **Même personnage**, graphie changée entre T1 et T2. `Madam Sharon` (T1 ch. 173–174) → `Miss Sharron` (T2 ch. 302). À unifier en alias. |
| `Klein Moretti` (146) | `Klien Moretti` (0 dans le texte) | 146 / 0 | Variante **présente seulement dans les noms de fichiers d'image** (`V01 Klien Moretti (Early Stage).jpg`, `V05 Character - Klien Moretti.jpg`). Ne pas créer d'entité « Klien ». |
| `Mr. Fool` (1 825) | `Mr Fool` (2) | 1 825 / 2 | Simple variante de ponctuation (`T2 ch. 221`, `T2 ch. 471`). |
| `Sherman` (59, T4) | `Shermane` (67, T5) | 59 / 67 | **Changement de prénom assumé** par le personnage (« you can use the name Shermane that you've already picked for yourself », T5 ch. 999) : modéliser comme alias temporel, pas comme faute. |
| `Tingen` (386) | `Tingen City` (120) | 386 / 120 | Forme courte / forme longue du même lieu. |
| `Obninsk` (17) | `Obninsks` (12) | 17 / 12 | Singulier / pluriel d'une créature (T3 ch. 720). |
| `Nighthawk` (168) | `Nighthawks` (525) | 168 / 525 | Organisation au singulier vs membres au pluriel — distinguer. |
| `Sealed Artifact` (701) | `Sealed Artifacts` (268) | 701 / 268 | Singulier/pluriel, pas une variante. |
| `Lord of Mysteries` | `Lord of the Mysteries` (122) | 1 407* / 122 | *Le premier chiffre est gonflé par les 1 394 titres `<head>` : après retrait, il reste des emplois réels. Le premier nomme le livre, le second la divinité (`T7 ch. 1272`) : **ne pas fusionner**. |
| `William` (42) | `Williams` (68) | 42 / 68 | **Faux positif** : `William I` (roi), `boss Williams`, `Williams Street` = référents distincts. |

Autres variants détectés mais non confirmés comme telles (pluriels et flexions majoritairement) : `Characteristics/Characteristic`, `Marionettist/Marionettists`, `Beyonder/Beyonders`, `Sequences/Sequencer`. À traiter par le modèle linguistique, pas par une table d'alias.

---

## 9. Recommandations pour l'extracteur

1. **Spine autoritaire = `toc.ncx`**. Filtrer `navLabel/text` avec `^Chapter\s+(\d+)\s*:\s*(.+)$` ; clé primaire = le numéro global `n` (1–1394), titre = le reste du libellé, source = `content/@src`. Ne jamais dériver `n` du suffixe `index_split_NNN`.
2. **Contrôles d'intégrité au chargement** : vérifier 1 394 chapitres uniques, continuité 1–1394, et `n == <h1>` du fichier source. Les 8 EPUB passent ces contrôles sans exception ; tout écart futur doit alerter.
3. **Extraire `<body>` uniquement**. Ignorer `<head><title>` (1 394 préfixes parasites) et les `<meta>`/`<link>` CSS.
4. **Découpage du texte d'un chapitre** : prendre l'héritage textuel de `<h1>` (titre, stocké à part) puis des `<p class="block_6">` / `<p class="block_7">` ; s'arrêter au **premier** des marqueurs suivants : `<p class="block_8">`, `<ol class="list_">`, marqueur `Author[’']?s? Notes?:` / `TL Note:`, ou `<div class="calibre5" id="calibre_pb_N">`. Convertir `\t`/`&nbsp;` en espaces et collapse les blancs ; conserver les guillemets typographiques pour les citations littérales.
5. **Notes comme données structurées** : pour chaque appel `[k]` (`<a href="#id_C…">`), joindre le `<li id="id_C…">` correspondant, **en parcourant toutes les `<ol>` du fichier** (cas du ch. 1266). Ne pas inclure ces notes dans la chaîne de citation d'une preuve, mais les garder en champ séparé.
6. **Nettoyage ciblé, pas global** : supprimer les 3 injections publicitaires avec `(?i)read\s+(?:the\s+)?(?:next|more)\s+chapter(?:\s+on\s+(?:our\s+)?)?vipnovel(?:\.com)?` et **logger** la suppression ; remplacer `丨` par `'` quand il joue le rôle d'apostrophe (`丨Yes`, `It丨s`) ; signaler `IVe`, `1泠邮`, `伽` pour relecture humaine. Conserver les CJK des notes du ch. 1266.
7. **Ignorer tout le hors-numérotation pour le corpus de texte** : 105 `navPoint` + 68 splits non référencés, tous images sauf la TOC et l'afterword de T8. Si le wiki veut des fiches personnage/lieu, reconstruire les légendes depuis les `<img src>` URL-décodés et les marquer « non vérifié » jusqu'à confirmation par une citation de chapitre.
8. **Alias de noms** : table minimale `Sharon → Sharron`, `Mr Fool → Mr. Fool`, `Klein` (jamais `Klien`) ; alias temporel `Sherman → Shermane`. Interdire la fusion automatique de `William`/`Williams` et de `Lord of Mysteries`/`Lord of the Mysteries`.
9. **Citations de preuve** : le texte narratif étant propre et le mapping `chapitre → n` fiable, citer `livre Tn, chapitre n, <h1>title</h1>, <extrait anglais littéral du bloc 6/7>`. Éviter les extraits contenant `[n]`, `Author's Note` ou `vipnovel`.

---

## 10. Méthode et reproductibilité

- Python 3.13, standard library uniquement : `zipfile` pour lire les EPUB, `re` pour les `navPoint`/`<h1>`/marqueurs, `html.parser` (`HTMLParser`, `convert_charrefs=True`) pour le texte. Aucune dépendance installée.
- Chaque volume a été parcouru intégralement (1 559 fichiers HTML, 1 499 `navPoint`, 1 394 chapitres) ; les chiffres ci-dessus sont des comptages exhaustifs, pas des échantillons. Les exemples littéraux sont cités avec leur volume, leur numéro de chapitre et leur fichier `index_split_*.html`.
- Les scripts d'analyse ont été exécutés dans `.scratch/` (ignoré par git) ; ils ne font pas partie du livrable. La logique de contrôle est décrite au §9 et peut être réimplémentée en une vingtaine de lignes.
- Sources primaires : les 8 EPUB du dépôt (`*.epub`, ignorés par git), en particulier `content.opf` (métadonnées calibre 5.44.0, `dc:language = en`), `toc.ncx` (catalogue) et `index_split_*.html` (texte).
