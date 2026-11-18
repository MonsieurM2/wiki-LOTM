# Entity taxonomy and alias policy

The wiki must give a fiche to every named referent in the eight English volumes without inventing content or producing unstable identifiers. We fixed a closed set of eight entity types (Character, Event, Chapter, Faction, Location, Artifact, Pathway, Concept), gave each Entity exactly one primary type plus optional Tags, and grant a fiche to any proper name occurring in narrative body text with no minimum mention count. Names found only in footnotes, author/TL notes or image filenames remain Candidates until a Chapter confirms them by Evidence; one canonical name carries Aliases, time-bounded when the character changes name in the story, and string equality never merges distinct referents. This trades a very large number of thin fichés for full coverage and evidence-backed identity.

## Considered and rejected

- **A minimum mention threshold**: rejected — it would silently drop the minor referents the destination explicitly includes.
- **Several primary types per Entity**: rejected — identifiers would shift whenever a referent is both a person and a deity (Mr. Fool, The Fool).
- **Automatic merging of identical or near-identical strings**: rejected — `William`/`Williams`, and `Lord of Mysteries` the book versus `Lord of the Mysteries` the deity, are different referents.
- **Image filenames as evidence**: rejected — the EPUB audit showed they are URL-encoded image names such as `Klien Moretti.jpg`, with no chapter number and no quote.
