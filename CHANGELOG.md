## Bibframe Changelog

### Bibframe 2.1
Major release

Note about version numbering:  Semantic versioning is desired, but not feasible
at this time. While we do not want to make a habit of making decimal releases 
major releases, we cannot guarantee this will not happen again.  There are
other elements of the ecosystem that need to be cleanly divorced from the 2.x release 
pattern before we can implement semantic versioning for the ontology.

Link: [http://id.loc.gov/ontologies/bibframe-2-1-0](http://id.loc.gov/ontologies/bibframe-2-1-0)

Github issues closed: 
 * https://github.com/lcnetdev/bibframe-ontology/issues/2
 * https://github.com/lcnetdev/bibframe-ontology/issues/3
 * https://github.com/lcnetdev/bibframe-ontology/issues/4
 * https://github.com/lcnetdev/bibframe-ontology/issues/8
 * https://github.com/lcnetdev/bibframe-ontology/issues/9
 * https://github.com/lcnetdev/bibframe-ontology/issues/11
 * https://github.com/lcnetdev/bibframe-ontology/issues/12
 * https://github.com/lcnetdev/bibframe-ontology/issues/16
 * https://github.com/lcnetdev/bibframe-ontology/issues/17
 * https://github.com/lcnetdev/bibframe-ontology/issues/19
 * https://github.com/lcnetdev/bibframe-ontology/issues/20
 * https://github.com/lcnetdev/bibframe-ontology/issues/21
 * https://github.com/lcnetdev/bibframe-ontology/issues/22
 * https://github.com/lcnetdev/bibframe-ontology/issues/23
 * https://github.com/lcnetdev/bibframe-ontology/issues/24
 * https://github.com/lcnetdev/bibframe-ontology/issues/25
 * https://github.com/lcnetdev/bibframe-ontology/issues/26
 * https://github.com/lcnetdev/bibframe-ontology/issues/28
 * https://github.com/lcnetdev/bibframe-ontology/issues/29
 * https://github.com/lcnetdev/bibframe-ontology/issues/30
 * https://github.com/lcnetdev/bibframe-ontology/issues/31
 * https://github.com/lcnetdev/bibframe-ontology/issues/34
 * https://github.com/lcnetdev/bibframe-ontology/issues/35
 * https://github.com/lcnetdev/bibframe-ontology/issues/37
 * https://github.com/lcnetdev/bibframe-ontology/issues/38
 * https://github.com/lcnetdev/bibframe-ontology/issues/39
 * https://github.com/lcnetdev/bibframe-ontology/issues/40
 * https://github.com/lcnetdev/bibframe-ontology/issues/41
 * https://github.com/lcnetdev/bibframe-ontology/issues/44
 * https://github.com/lcnetdev/bibframe-ontology/issues/50
 * https://github.com/lcnetdev/bibframe-ontology/issues/51
 * https://github.com/lcnetdev/bibframe-ontology/issues/52
 * https://github.com/lcnetdev/bibframe-ontology/issues/53
 * https://github.com/lcnetdev/bibframe-ontology/issues/55
 * https://github.com/lcnetdev/bibframe-ontology/issues/56
 * https://github.com/lcnetdev/bibframe-ontology/issues/57
 * https://github.com/lcnetdev/bibframe-ontology/issues/58
 * https://github.com/lcnetdev/bibframe-ontology/issues/59
 * https://github.com/lcnetdev/bibframe-ontology/issues/60
 * https://github.com/lcnetdev/bibframe-ontology/issues/61
 * https://github.com/lcnetdev/bibframe-ontology/issues/62
 * https://github.com/lcnetdev/bibframe-ontology/issues/63
 * https://github.com/lcnetdev/bibframe-ontology/issues/64
 * https://github.com/lcnetdev/bibframe-ontology/issues/66
 * https://github.com/lcnetdev/bibframe-ontology/issues/67
 * https://github.com/lcnetdev/bibframe-ontology/issues/75
 * https://github.com/lcnetdev/bibframe-ontology/issues/76
 * https://github.com/lcnetdev/bibframe-ontology/issues/77
 * https://github.com/lcnetdev/bibframe-ontology/issues/78
 * 
 
Changes
  * Changes to Existing Classes
    * [AccessionNumber - New](commit)
    * [AppliedMaterial - Changed subclass to Material](commit)
    * [Arrangement - Redefined](commit)
    * [BaseMaterial - Changed subclass to Material](commit)
    * [Classification - Added editorial note](commit)
    * [Eidr - New](commit)
    * [Ensemble - New](commit)
    * [Event - Broaden definition](commit)
    * [GenreForm - Broaden definition](commit)
    * [Hub - New](commit)
    * [Identifier - Added editorial note](commit)
    * [Material - New](commit)
    * [Mount - Amended definition](commit)
    * [MovementNotation - Modified label](commit)
    * [MusicEnsemble - Changed subclass to Ensemble](commit)
    * [MusicNotation - Modified label](commit)
    * [Note - Added editorial note](commit)
    * [PubFrequency - New](commit)
    * [Script - Modified label](commit)
    * [TactileNotation - Modified label](commit)
    * [Urn - Corrected definition](commit)
  * Changes to Object Properties
    * [acquisitionSource - Removed range](commit)
    * [adminMetadataFor - New](commit)
    * [agent - Removed range](commit)
    * [agentOf - New](commit)
    * [appliedMaterial - Removed range](commit)
    * [appliedMaterial - Broadened domain](commit)
    * [appliedMaterial - Made subproperty of material](commit)
    * [appliedMaterialOf - New](commit)
    * [arrangement - Redefined](commit)
    * [arrangementOf - New](commit)
    * [assigner - Broaden domain](commit)
    * [assigner - Removed range](commit)
    * [baseMaterial - Removed range](commit)
    * [baseMaterial - Broadened domain](commit)
    * [baseMaterial - Made subproperty of material](commit)
    * [baseMaterialOf - New](commit)
    * [collectionArrangement - New](commit)
    * [collectionArrangementOf - New](commit)
    * [colorContent - Broaden range](commit)
    * [contributionOf - New](commit)
    * [derivedFrom - Removed range](commit)
    * [descriptionModifier - Removed range](commit)
    * [electronicLocator - Removed domain](commit)
    * [expressionOf - Modified definition](commit)
    * [extent - Broadened range](commit)
    * [fontSize - Added note](commit)
    * [frequency - Removed domain](commit)
    * [genreForm - Removed range](commit)
    * [geographicCoverage - Removed domain](commit)
    * [grantingInstitution - Removed range](commit)
    * [hasExpression - Modified definition](commit)
    * [hasPart - Use with Event also](commit)
    * [heldBy - Removed range](commit)
    * [material - New](commit)
    * [materialOf - New](commit)
    * [mount - Modified label](commit)
    * [noteFor - New](commit)
    * [originPlace - Better align definition with property name](commit)
    * [originPlace - Removed range](commit)
    * [partOf - Use with Event also](commit)
    * [place - Removed range](commit)
    * [pubFrequency - New](commit)
    * [source - Removed range](commit)
    * [subject - Broadened domain](commit)
    * [subjectOf - New](commit)
    * [title - Broadened domain](commit)
    * [titleOf - New](commit)
  * Changes to Datatype Properties
    * [awards - Added note](commit)
    * [collectionOrganization - New](commit)
    * [custodialHistory - Added note](commit)
    * [dimensions - Added note](commit)
    * [firstIssue - Removed domain](commit)
    * [hierarchicalLevel - Modified range](commit)
    * [lastIssue - Removed domain](commit)
    * [originDate - Better align definition with property name](commit)
    * [pattern - Modified range](commit)

---

### Bibframe 2.0.1
Patch Release

Link: [http://id.loc.gov/ontologies/bibframe-2-0-1](http://id.loc.gov/ontologies/bibframe-2-0-1)

Github issues closed: 
 * https://github.com/lcnetdev/bibframe-ontology/issues/7
 * https://github.com/lcnetdev/bibframe-ontology/issues/42
 
Changes
  * Changes to Existing Classes 
    * [MixedMaterial - clarification](https://github.com/lcnetdev/bibframe-ontology/commit/f447b507dcb58d95bb34617886e43f3ac7565098#diff-a63046abd708bb861aa910d97bf42005)
    * [PublisherNumber - clarification](https://github.com/lcnetdev/bibframe-ontology/commit/f447b507dcb58d95bb34617886e43f3ac7565098#diff-1a032606aef2cdee819b56960646ad34)

  * Changes to Existing ObjectProperty 
    * [identifies - typo](https://github.com/lcnetdev/bibframe-ontology/commit/f447b507dcb58d95bb34617886e43f3ac7565098#diff-186fef12f7006b3275b1f23f900ee65e)

---

### Bibframe 2.0.0
Initial Release

Link: [http://id.loc.gov/ontologies/bibframe-2-0-0](http://id.loc.gov/ontologies/bibframe-2-0-0)


