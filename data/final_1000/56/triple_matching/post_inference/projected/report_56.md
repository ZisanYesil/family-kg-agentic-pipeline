# Triple matching report: 56

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Heather_Headley | hasAwardReceived | Tony_Award_for_Best_Actress_in_a_Musical |
| Heather_Headley | type | Agent |
| In_My_Mind | hasCreator | Heather_Headley |
| In_My_Mind | hasPerformer | Heather_Headley |
| In_My_Mind | type | Artifact |
| In_My_Mind | type | CreativeWork |
| Tony_Award_for_Best_Actress_in_a_Musical | type | Award |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Heather_Headley | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.875000 |
| Recall | 1.000000 |
| F1 score | 0.933333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
