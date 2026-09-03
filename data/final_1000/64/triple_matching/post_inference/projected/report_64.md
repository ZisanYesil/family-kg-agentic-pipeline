# Triple matching report: 64

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Bertrand_of_Toulouse | hasChild | Pons |
| Bertrand_of_Toulouse | type | Agent |
| Bertrand_of_Toulouse | type | Person |
| Cecile_of_France | hasSpouse | Pons |
| Cecile_of_France | type | Agent |
| Cecile_of_France | type | Person |
| Pons | hasParent | Bertrand_of_Toulouse |
| Pons | hasSpouse | Cecile_of_France |
| Pons | type | Agent |
| Pons | type | Person |

# 2. Unmatched triples

**Total unmatched count: 0**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 10 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 0 |
| Precision | 1.000000 |
| Recall | 1.000000 |
| F1 score | 1.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
