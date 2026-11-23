# Bone and Brass — *The Osteological Cabinet*

Cabinet d'anatomie occulte : blanc osseux, laiton d'instrument, noir clinique, étiquettes de musée, rigueur du compas.

**Palette :** Clinique `#0D0F10` (fond), Os `#E7E0CE` (texte), Laiton `#A98A48` (filets), Ivoire `#CDC5B0` (cartouches), Moelle `#7C4034` (accent occulte).

**Typographie :** Spectral, corps 16px/1.65 ; titres en petites capitales espacées, chiffres tabulaires pour les cotes.

**Motif custom :** fémur et compas gradué SVG en filigrane, trait fin, encoches de mesure le long de l'os — ornement global unique, jamais par fiche.

**Décisions :**
1. `.gloss` = étiquette muséale : cartouche Ivoire cerné d'un double filet Laiton, coins d'onglet SVG.
2. `.entity` : `::before` règle graduée en `repeating-linear-gradient` Laiton, tiret sous le titre.
3. `.brand-mark` devient le compas-fémur SVG, `opacity:.1` derrière l'en-tête — aucun logo copié, pas d'image par fiche.

**Risque :** l'Os sur Clinique peut éblouir ; désaturer, valider AA sur corps et étiquettes.
