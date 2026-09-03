# Triple matching report: 392

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Richard_Pottier | hasDeathPlace | Le_Plessis_Bouchard |
| The_Beautiful_Otero | hasDirector | Richard_Pottier |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Le_Plessis_Bouchard | type | Place |
| Le_Plessis_Bouchard | type | NamedIndividual |
| Le_Plessis_Bouchard | label | "Le Plessis-Bouchard" |
| Richard_Pottier | type | Person |
| Richard_Pottier | type | NamedIndividual |
| Richard_Pottier | label | "Richard Pottier" |
| The_Beautiful_Otero | type | Film |
| The_Beautiful_Otero | type | NamedIndividual |
| The_Beautiful_Otero | label | "The Beautiful Otero" |
| The_Beautiful_Otero | altLabel | "La bella Otero" |
| The_Beautiful_Otero | altLabel | "La belle Otero" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
