# Triple matching report: 670

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alfonso_XI_of_Castile | hasParent | Ferdinand_IV_of_Castile |
| Ferdinand_IV_of_Castile | hasDeathPlace | Jaén |

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
| Alfonso_XI_of_Castile | type | Person |
| Alfonso_XI_of_Castile | type | NamedIndividual |
| Alfonso_XI_of_Castile | label | "Alfonso XI of Castile" |
| Ferdinand_IV_of_Castile | type | Person |
| Ferdinand_IV_of_Castile | type | NamedIndividual |
| Ferdinand_IV_of_Castile | label | "Ferdinand IV of Castile" |
| Jaén | type | Place |
| Jaén | type | NamedIndividual |
| Jaén | label | "Jaén" |

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
