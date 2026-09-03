# Triple matching report: 8

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Karin_Stoltenberg | hasSpouse | Thorvald_Stoltenberg |
| Thorvald_Stoltenberg | hasEmployer | United_Nations |

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
| Karin_Stoltenberg | type | Person |
| Karin_Stoltenberg | type | NamedIndividual |
| Karin_Stoltenberg | label | "Karin Stoltenberg" |
| Thorvald_Stoltenberg | type | Person |
| Thorvald_Stoltenberg | type | NamedIndividual |
| Thorvald_Stoltenberg | label | "Thorvald Stoltenberg" |
| United_Nations | type | Organization |
| United_Nations | type | NamedIndividual |
| United_Nations | label | "United Nations" |

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
