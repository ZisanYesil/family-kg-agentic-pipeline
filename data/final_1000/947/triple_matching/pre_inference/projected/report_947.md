# Triple matching report: 947

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gianfranco_Parolini | hasDeathPlace | Rome |
| God_s_Gun | hasDirector | Gianfranco_Parolini |

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
| Gianfranco_Parolini | type | Person |
| Gianfranco_Parolini | type | NamedIndividual |
| Gianfranco_Parolini | label | "Gianfranco Parolini" |
| Gianfranco_Parolini | altLabel | "Frank Kramer" |
| God_s_Gun | type | Film |
| God_s_Gun | type | NamedIndividual |
| God_s_Gun | label | "God's Gun" |
| Rome | type | Place |
| Rome | type | NamedIndividual |
| Rome | label | "Rome" |
| Rome | altLabel | "Rome, Italy" |

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
