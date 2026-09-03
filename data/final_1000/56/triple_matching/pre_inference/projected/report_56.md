# Triple matching report: 56

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Heather_Headley | hasAwardReceived | Tony_Award_for_Best_Actress_in_a_Musical |
| In_My_Mind | hasPerformer | Heather_Headley |

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
| Heather_Headley | type | Person |
| Heather_Headley | type | NamedIndividual |
| Heather_Headley | label | "Heather Headley" |
| In_My_Mind | type | CreativeWork |
| In_My_Mind | type | NamedIndividual |
| In_My_Mind | label | "In My Mind (Heather Headley song)" |
| Tony_Award_for_Best_Actress_in_a_Musical | type | Award |
| Tony_Award_for_Best_Actress_in_a_Musical | type | NamedIndividual |
| Tony_Award_for_Best_Actress_in_a_Musical | label | "Tony Award for Best Actress in a Musical" |

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
