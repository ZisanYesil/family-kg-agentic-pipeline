# Triple matching report: 992

# 1. Matched triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Clara_Law | type | Agent |
| Clara_Law | type | Person |
| I_ll_Get_By_film | hasCreator | Richard_Sale |
| I_ll_Get_By_film | hasDirector | Richard_Sale |
| I_ll_Get_By_film | type | Artifact |
| I_ll_Get_By_film | type | CreativeWork |
| I_ll_Get_By_film | type | Film |
| Richard_Sale | type | Agent |
| Richard_Sale | type | Person |
| The_Reincarnation_of_Golden_Lotus | hasCreator | Clara_Law |
| The_Reincarnation_of_Golden_Lotus | hasDirector | Clara_Law |
| The_Reincarnation_of_Golden_Lotus | type | Artifact |
| The_Reincarnation_of_Golden_Lotus | type | CreativeWork |
| The_Reincarnation_of_Golden_Lotus | type | Film |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Australia | type | Country |
| Australia | type | Place |
| Clara_Law | hasCountry | Australia |
| Richard_Sale_director | hasCountry | American |
| Richard_Sale_director | type | Agent |
| Richard_Sale_director | type | Person |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Clara_Law | hasCountry | country_hong_kong |
| Richard_Sale | hasCountry | American |
| country_hong_kong | type | Country |
| country_hong_kong | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 22 |
| Union triples in scope | 26 |
| True positives (matched) | 16 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.800000 |
| Recall | 0.727273 |
| F1 score | 0.761905 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
