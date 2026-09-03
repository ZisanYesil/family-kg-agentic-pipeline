# Triple matching report: 836

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| César_Award_for_Best_Director | type | Award |
| Luc_Besson | hasAwardReceived | César_Award_for_Best_Director |
| Luc_Besson | type | Agent |
| Luc_Besson | type | Person |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | hasCreator | Luc_Besson |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | hasDirector | Luc_Besson |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | type | Artifact |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | type | CreativeWork |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | type | Film |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Luc_Besson | hasAwardReceived | award_best_french_director |
| award_best_french_director | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.818182 |
| Recall | 1.000000 |
| F1 score | 0.900000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
