# Triple matching report: 836

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Luc_Besson | hasAwardReceived | César_Award_for_Best_Director |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | hasDirector | Luc_Besson |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| César_Award_for_Best_Director | type | Award |
| César_Award_for_Best_Director | type | NamedIndividual |
| César_Award_for_Best_Director | label | "Best Director" |
| Luc_Besson | hasAwardReceived | award_best_french_director |
| Luc_Besson | type | Person |
| Luc_Besson | type | NamedIndividual |
| Luc_Besson | label | "Luc Besson" |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | type | Film |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | type | NamedIndividual |
| The_Extraordinary_Adventures_of_Adèle_Blanc_Sec | label | "The Extraordinary Adventures of Adèle Blanc‑Sec" |
| award_best_french_director | type | Award |
| award_best_french_director | type | NamedIndividual |
| award_best_french_director | label | "Best French Director" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
