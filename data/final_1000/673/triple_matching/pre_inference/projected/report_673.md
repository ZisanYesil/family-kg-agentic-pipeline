# Triple matching report: 673

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Herman_Frasch | hasBirthPlace | Oberrot |
| Union_Sulphur_Company | hasFounder | Herman_Frasch |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Herman_Frasch | type | Person |
| Herman_Frasch | type | NamedIndividual |
| Herman_Frasch | label | "Herman Frasch" |
| Oberrot | type | Place |
| Oberrot | type | NamedIndividual |
| Oberrot | label | "Oberrot bei Gaildorf, Württemberg" |
| Union_Sulphur_Company | type | Organization |
| Union_Sulphur_Company | type | NamedIndividual |
| Union_Sulphur_Company | label | "Union Sulphur Company" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
