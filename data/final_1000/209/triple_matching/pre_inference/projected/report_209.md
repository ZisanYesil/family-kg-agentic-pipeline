# Triple matching report: 209

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| T_I | hasOccupation | actor |
| T_I | hasOccupation | rapper |
| Wayne_Maki | hasOccupation | ice_hockey_player |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| T_I | type | Person |
| T_I | type | NamedIndividual |
| T_I | label | "Clifford Joseph Harris Jr." |
| T_I | altLabel | "T.I." |
| T_I | altLabel | "Tip" |
| Wayne_Maki | type | Person |
| Wayne_Maki | type | NamedIndividual |
| Wayne_Maki | label | "Wayne Maki" |
| actor | type | Occupation |
| actor | type | NamedIndividual |
| actor | label | "actor" |
| ice_hockey_player | type | Occupation |
| ice_hockey_player | type | NamedIndividual |
| ice_hockey_player | label | "ice hockey player" |
| rapper | type | Occupation |
| rapper | type | NamedIndividual |
| rapper | label | "rapper" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 20 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.150000 |
| Recall | 1.000000 |
| F1 score | 0.260870 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
