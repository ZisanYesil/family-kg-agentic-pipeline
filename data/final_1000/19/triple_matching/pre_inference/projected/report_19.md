# Triple matching report: 19

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Edward_I_of_England | hasParent | Henry_III |
| Henry_III | hasSpouse | Eleanor_of_Provence |

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
| Edward_I_of_England | type | Person |
| Edward_I_of_England | type | NamedIndividual |
| Edward_I_of_England | label | "Edward I of England" |
| Eleanor_of_Provence | type | Person |
| Eleanor_of_Provence | type | NamedIndividual |
| Eleanor_of_Provence | label | "Eleanor of Provence" |
| Henry_III | type | Person |
| Henry_III | type | NamedIndividual |
| Henry_III | label | "Henry III of England" |

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
