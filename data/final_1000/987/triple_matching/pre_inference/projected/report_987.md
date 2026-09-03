# Triple matching report: 987

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Glimpses_Impressions | hasDirector | Jean_François_Pouliot |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jean_François_Pouliot | hasEmployer | National_Film_Board |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Glimpses_Impressions | type | Film |
| Glimpses_Impressions | type | NamedIndividual |
| Glimpses_Impressions | label | "Glimpses/Impressions" |
| Jean_François_Pouliot | type | Person |
| Jean_François_Pouliot | type | NamedIndividual |
| Jean_François_Pouliot | label | "Jean-François Pouliot" |
| organization_cossette_communication_marketing | hasMember | Jean_François_Pouliot |
| organization_cossette_communication_marketing | type | Organization |
| organization_cossette_communication_marketing | type | NamedIndividual |
| organization_cossette_communication_marketing | label | "Cossette Communication Marketing" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
