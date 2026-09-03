# Triple matching report: 64

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pons | hasSpouse | Cecile_of_France |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bertrand_of_Toulouse | hasChild | Pons |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Bertrand_of_Toulouse | type | Person |
| Bertrand_of_Toulouse | type | NamedIndividual |
| Bertrand_of_Toulouse | label | "Bertrand, Count of Toulouse" |
| Bertrand_of_Toulouse | altLabel | "Bertrand of Toulouse" |
| Cecile_of_France | type | Person |
| Cecile_of_France | type | NamedIndividual |
| Cecile_of_France | label | "Cecile of France" |
| Cecile_of_France | altLabel | "Cecile" |
| Pons | hasParent | Bertrand_of_Toulouse |
| Pons | type | Person |
| Pons | type | NamedIndividual |
| Pons | label | "Pons, Count of Tripoli" |
| Pons | altLabel | "Pons" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
