# Triple matching report: 987

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Glimpses_Impressions | hasCreator | Jean_François_Pouliot |
| Glimpses_Impressions | hasDirector | Jean_François_Pouliot |
| Glimpses_Impressions | type | Artifact |
| Glimpses_Impressions | type | CreativeWork |
| Glimpses_Impressions | type | Film |
| Jean_François_Pouliot | type | Agent |
| Jean_François_Pouliot | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Jean_François_Pouliot | hasEmployer | National_Film_Board |
| National_Film_Board | type | Agent |
| National_Film_Board | type | Organization |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| organization_cossette_communication_marketing | hasMember | Jean_François_Pouliot |
| organization_cossette_communication_marketing | type | Agent |
| organization_cossette_communication_marketing | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 13 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.700000 |
| Recall | 0.700000 |
| F1 score | 0.700000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
