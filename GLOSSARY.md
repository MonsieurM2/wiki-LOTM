# Lord of the Mysteries Wiki

The domain model of the verified wiki built from the eight English LOTM volumes: every named referent earns a fiche, and every fact is anchored to literal evidence. This glossary fixes the vocabulary used by tickets, data and site alike.

## Core concepts

**Entity**:
A named referent in the narrative that receives its own fiche, whatever its importance.
_Avoid_: page, node, item, character (when the referent is not a person)

**Mention**:
An occurrence of a name in the narrative body of a chapter.
_Avoid_: reference, occurrence, appearance

**Evidence**:
The book number, chapter number and literal English quote that justify a fact.
_Avoid_: citation, source, proof

**Alias**:
An alternative surface form of an Entity's canonical name, optionally valid only in a stated period.
_Avoid_: nickname, alternate name, typo

**Event**:
A narrated happening with at least one identifiable participant, anchored to a Chapter by Evidence.
_Avoid_: action, beat, occurrence

**Chapter**:
A numbered narrative unit (1–1394) that is both an Entity and the spine the wiki navigates by.
_Avoid_: volume, section, split

**Candidate**:
A name harvested outside the narrative body, such as an image filename, that becomes an Entity only once a Chapter confirms it by Evidence.
_Avoid_: unverified entity, phantom, placeholder

**Tag**:
A secondary classification on an Entity that does not change its primary type.
_Avoid_: secondary type, category, label

**Sequence Title**:
A named rank within a Pathway, such as Seer or Clown; its Entity has Concept as primary type and carries a `sequence-title` Tag, since the taxonomy is closed at eight types.
_Avoid_: rank, level, Sequence 9

## Entity types

**Character**:
An Entity that is an individual person or person-like being.
_Avoid_: person, actor

**Faction**:
An Entity that is an organization, club or group with a collective identity.
_Avoid_: organization, guild, team

**Location**:
An Entity that is a named place.
_Avoid_: place, region

**Artifact**:
An Entity that is a named physical object, including a Sealed Artifact or an in-universe book.
_Avoid_: item, object, equipment

**Pathway**:
An Entity that is a named supernatural route of advancement, such as The Fool.
_Avoid_: route, path, sequence (when the whole route is meant)

**Concept**:
An Entity that is a named idea, power, phenomenon or title that is not a person, place, object, event or Pathway.
_Avoid_: idea, abstraction, topic
