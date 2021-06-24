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
 * https://github.com/lcnetdev/bibframe-ontology/issues/79
 
Changes
  * Changes to Existing Classes
    * [AccessionNumber - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-76055b692f80bde0c6d4c3066b4386be0b6b0697f19c846c5d0d1a49aedf097d)
    * [AppliedMaterial - Changed subclass to Material](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-0733f79cede9066c0f019d8fa86851185452955a2b0631948ad8658b7e9fe482)
    * [Arrangement - Redefined](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-ac9ccfbf49cdb993996bc55ee99ff585182dae877ec62ed96e10d343f393562f)
    * [BaseMaterial - Changed subclass to Material](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-1c7cdb7f82a15828696be2b29887066990d2c5862594e94a061d68fdb1363f0a)
    * [Classification - Added editorial note](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-2f2c33ac52c80cc9a5ed919603b518bbe76b4cd51ff031d8b90ba000e8cca9f1)
    * [CollectionArrangement - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-445f9c1ce0e7cc8198d88b7b10d325895229f335a34e998192b23aa08793b93d)
    * [Eidr - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-d7c9cf886242159fe29c43bcc735e4940ca93661f6f2135d2ab273043dbeead1)
    * [Ensemble - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-1056513e3d92297600f861398fdaf5e260fe2fbbe99ef1bbd6432dc2764b0d87)
    * [Event - Broaden definition](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-edb38b2bf6773d80221adb87c9cfe812e54f253102249d04e631bab523b4243e)
    * [GenreForm - Broaden definition](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-dc62e351d505353ba658a3cc868baa2248ed80452c801226b67e4fd9e8f4025a)
    * [Hub - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-2acf34ef2b299ebe49369db47ee142a2e1512f6cd8a8045e1d660eaf2f85b5aa)
    * [Identifier - Added editorial note](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-70374a3eb6fe321efc1df40c272f51d442c80e3ecd06c532a6fe6c72e8ee4b4f)
    * [Material - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-863b5d1e72429d55e1920bb928d0fcf8216c689ab951459e5a7f02627b071391)
    * [Mount - Amended definition](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-54fba12f18aea10ccf9115c4e74a613cfdb9d03e7dd7ec5dc6e63716683c9f96)
    * [MovementNotation - Modified label](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-9b79a123848b5084e707cbe4d3f1a1aa8487f15972bc71ac2bc7ade7787f2d9f)
    * [MusicEnsemble - Changed subclass to Ensemble](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-bddf890c0e413200b9321f147427425cf6227aeb16da29cf46c642eb3aca9bef)
    * [MusicNotation - Modified label](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-df28de22fecf2f91ae798f844cbd5cfcbf08adebc5eab22b377e15a05578d546)
    * [Note - Added editorial note](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-36495bcf6664c6a3a6dea2c316822e7566e4b2ba6710cec42824ef0b075f7044)
    * [PubFrequency - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-d398189c43d99ed65af6f555bf596ebe08ece8dafea7eb78cadcfcfce7ac67c1)
    * [Script - Modified label](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-4c5baf34b708938f510514f19a2b65dc76b582be2d32543a0e51f1550a3754ec)
    * [TactileNotation - Modified label](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-49ef30fc8e9995f4f63f8d5c1d1223425112cdc54c7e4ea32bb6d5ef7757ffc1)
    * [Urn - Corrected definition](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-adec4708c0ce6748df6a91fc3b971ebe6c619df90ddb5f87da9dda27a6e6d577)
  * Changes to Object Properties
    * [acquisitionSource - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-ee6be50f1f0cac1dbe6cf734552e69a72a6766e84f0ccff63929d1ed7def629a)
    * [adminMetadataFor - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-cd75bc8e190e90ce5de90d90bf66fc745b50b9beb320b43d4e175243aec690b3)
    * [agent - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-700dbc00a918dc57b3de2394828fd292df27b4fa580895a2a94752b049b0b375)
    * [agentOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-dc7942a79fd5521b98d991c4c13a6aecff39de5d2068e9a4f00b3a3c1efa4b31)
    * [appliedMaterial - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-bdb3ab43e8d4c6f69063e12952de1a58ac039f9778e595c557e75171bf4282d4)
    * [appliedMaterial - Broadened domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-bdb3ab43e8d4c6f69063e12952de1a58ac039f9778e595c557e75171bf4282d4)
    * [appliedMaterial - Made subproperty of material](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-bdb3ab43e8d4c6f69063e12952de1a58ac039f9778e595c557e75171bf4282d4)
    * [appliedMaterialOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-eccbd14e8833d1167dc5d503dbc9c2a6eca02f7e0429f8edeeb012e377f15d83)
    * [arrangement - Redefined](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-baeeada0ea1f90bc2d4ed9f0a1be585c9a4fb1e962e135e9b72719402b209b2a)
    * [arrangementOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-1eb31d5e06c404cbf4d5d0dab179748405b60ed247adcf763a8d3347bdedffc3)
    * [assigner - Broaden domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-3e36dffc5cdc20b6053db9d337c2d3b56ace82cc8c0bab1ad0c60dc6c297ffd7)
    * [assigner - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-3e36dffc5cdc20b6053db9d337c2d3b56ace82cc8c0bab1ad0c60dc6c297ffd7)
    * [baseMaterial - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-b8c839ad338153a2439efc59ff4a7c6b154621abf9bd439f7da1984aacab092e)
    * [baseMaterial - Broadened domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-b8c839ad338153a2439efc59ff4a7c6b154621abf9bd439f7da1984aacab092e)
    * [baseMaterial - Made subproperty of material](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-b8c839ad338153a2439efc59ff4a7c6b154621abf9bd439f7da1984aacab092e)
    * [baseMaterialOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-481f908983d59b5ce4174f640559ce72bd1c0bf73a033ed5c093abb741fdd032)
    * [collectionArrangement - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-f81f05eba25781638ffcac82dd718a56f439409e96a10b315ff76da4d8fdd8c4)
    * [collectionArrangementOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-d25604734f631f6fa3687844112125dd83ed80aa15e71467b11d00f6a2367cfd)
    * [colorContent - Broaden range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-9d2c354f38b8bcb4e097e66a144d9d71a9ed6054011cf20cba8c051db88725e0)
    * [contributionOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-229e14bddeaee668350625813d50045310a0bbd848276795c810d2ff7c6ee87e)
    * [derivedFrom - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-44bc9155cc2e380cf3d96e37bd24983e2eb4df175a725dcfbffa5bbefd547d2c)
    * [descriptionModifier - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-82d7ce3ec407d421494ce63fbf0367868c001014da13e4418ac3c3d5f3b3d523)
    * [electronicLocator - Removed domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-1c72a7954b8ea53e788b7ca781468bb25ea29dc7d11f2fc6c34718bf59d85627)
    * [expressionOf - Modified definition](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-8b06e923390c02039fc58b9f3bda6bd49b45087d4225f82080dea043f005ae6c)
    * [extent - Broadened range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-0480aafbbb0553efb42d75dfb0915fbbd03174bd330cfcc68509d40264d7df8d)
    * [fontSize - Added note](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-c4345271515390d39bf8c48684b6bfcc1164ca41e164d99983e0311cb7068c8a)
    * [frequency - Removed domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-acea35de9aad934f26d0dfcf2d049294d5ca20e63733f545499115be8989a618)
    * [genreForm - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-156d994501de9f12e05c61e8fe6e5e541b7700066968b36200af56443dd98caf)
    * [geographicCoverage - Removed domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-b05d9deed7be84cbf43439cede026383f037fe685558f7b553eced82a84985b2)
    * [grantingInstitution - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-3a3b90efdfb0de79fce217d1954eeec84b4af1cee9b2d208424c631d3def07b7)
    * [hasExpression - Modified definition](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-e5bcfe2f0cbbeca8433b284c39c5a1bcaf1513b1c7ec3c7ddae01f9db86344e1)
    * [hasPart - Use with Event also](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-1a073ad90289938452234839c7c140463fd7432d2a4a8d57ac8a7c618b008e54)
    * [heldBy - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-353a5269fb79756bb88b6ab6ab00d2f92cb59cbb781135a6414d430fd22b7ae6)
    * [material - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-8eddfc04727cf811ab221ec69e42a2143230fed267a5c154c73d605174ad106a)
    * [materialOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-815bcfe0e8a5670cba6fed8110e7242fff80e9f49ba76ebff063a650478e12f4)
    * [mount - Modified label](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-8475c829628007cc97e9decb64188a165b3c214918cf4fd97db314c5b16a2266)
    * [noteFor - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-c669f2b698dd4a6ccae980599e2e95a77aa70224a0de8974c04f86b61eb7dd89)
    * [originPlace - Better align definition with property name](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-b700fe0b589f860f79ef3a8d7351a6b563e3c14bee6cf8dd2a9b9b506a0e9af3)
    * [originPlace - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-b700fe0b589f860f79ef3a8d7351a6b563e3c14bee6cf8dd2a9b9b506a0e9af3)
    * [partOf - Use with Event also](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-0363db3294308f2c81bfe8b20e1fe3e6c435275a9eec5af40ad6e9b6488c93ad)
    * [place - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-30fd56e061f62387a3e094f9c275234f10fb161d7b4d28cbbf58f11479259b22)
    * [pubFrequency - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-6644e3324522ed899d889af948d12bcf79db0949d446f3ae6cd4ee08f52d5258)
    * [source - Removed range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-ceec4c2e07ad6e33051aea3597ebe0bf58d4d67b2f64a69d71b593c2b0d5f408)
    * [subject - Broadened domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-a8e480230f20e2b45b8058ac7f9aa22b88c198d9676592340399bcace9fd5ebc)
    * [subjectOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-09077b4810a5e05a7039aa00a57007655a6019f5bed0bca08b57d8c0d271a1ef)
    * [title - Broadened domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-7a2bd1f7f288808b5c252715e1637b9be7ebb5c7828f271c199ee70d01953b47)
    * [titleOf - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-508528b0487bc875d1ece9fce5962b7c8a1d2386094913130ab8e58c154a1f70)
  * Changes to Datatype Properties
    * [awards - Added note](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-5529ff0955464c2da5225d02ea0ede77250ebeeb9e3ff72107236b7d41b69edd)
    * [collectionOrganization - New](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-c44262763c8caeadee57fea8d9e879defbe0c8e15e94351402a315a6aa564dd4)
    * [custodialHistory - Added note](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-243aa6a0621ac98913df1bf5c5212b686f20fbb12d4d28850ee121266aee8d43)
    * [dimensions - Added note](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-cad7ad29103f70c02667e1442c8603ec27ce81701a0bb30779208f4261df1bd8)
    * [firstIssue - Removed domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-33a7796b97a2d574cc30a84b6e3d8bf8302e79301bb036df3d99ad5291153098)
    * [hierarchicalLevel - Modified range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-d4e1e36d57977591deaf3eb6b1dd6fdc56d13dc1c031f5d3e0784d970a7ee692)
    * [lastIssue - Removed domain](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-7f91b0fb7d45cba09bb6d60c601ae6963e29ac1e62647bc0356d5ccc405ac03d)
    * [originDate - Better align definition with property name](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-2c819be42e4f24df4571e3e330683826dbf1f1f7477c47db7e637db2d8e11de9)
    * [pattern - Modified range](https://github.com/lcnetdev/bibframe-ontology/commit/65cac79f4cac4c379da76c2f55779f748c1dfb6a#diff-fd6f8a08228630a6cee6275065849f0550ead035c245b628d457641e90164706)

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


