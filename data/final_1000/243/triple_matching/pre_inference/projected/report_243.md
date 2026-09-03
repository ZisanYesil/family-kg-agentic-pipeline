# Triple matching report: 243

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hard_Time_Loving_You | hasPerformer | Julian_Austin |
| Julian_Austin | hasBirthPlace | Sussex |

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
| Hard_Time_Loving_You | type | CreativeWork |
| Hard_Time_Loving_You | type | NamedIndividual |
| Hard_Time_Loving_You | label | "Hard Time Loving You" |
| Julian_Austin | type | Person |
| Julian_Austin | type | NamedIndividual |
| Julian_Austin | label | "Julian Austin" |
| Sussex | type | Place |
| Sussex | type | NamedIndividual |
| Sussex | label | "Sussex, New Brunswick" |

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
