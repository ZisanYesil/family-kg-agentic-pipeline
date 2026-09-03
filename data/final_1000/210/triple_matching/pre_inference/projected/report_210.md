# Triple matching report: 210

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Michael_Mayer | hasAwardReceived | Tony_Award_for_Best_Direction_of_a_Musical |
| The_Seagull | hasDirector | Michael_Mayer |

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
| Michael_Mayer | type | Person |
| Michael_Mayer | type | NamedIndividual |
| Michael_Mayer | label | "Michael Mayer" |
| The_Seagull | type | Film |
| The_Seagull | type | NamedIndividual |
| The_Seagull | label | "The Seagull (2018 film)" |
| Tony_Award_for_Best_Direction_of_a_Musical | type | Award |
| Tony_Award_for_Best_Direction_of_a_Musical | type | NamedIndividual |
| Tony_Award_for_Best_Direction_of_a_Musical | label | "Tony Award for Best Direction of a Musical" |

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
