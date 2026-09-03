# Triple matching report: 530

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Back_Home | hasDirector | Piers_Haggard |
| Piers_Haggard | hasChild | Daisy_Haggard |

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
| Back_Home | type | Film |
| Back_Home | type | NamedIndividual |
| Back_Home | label | "Back Home" |
| Daisy_Haggard | type | Person |
| Daisy_Haggard | type | NamedIndividual |
| Daisy_Haggard | label | "Daisy Haggard" |
| Piers_Haggard | type | Person |
| Piers_Haggard | type | NamedIndividual |
| Piers_Haggard | label | "Piers Haggard" |

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
