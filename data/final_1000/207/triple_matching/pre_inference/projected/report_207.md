# Triple matching report: 207

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Michael_D_Antonovich | hasOccupation | politician |
| Péter_Máté | hasOccupation | composer |
| Péter_Máté | hasOccupation | pianist |
| Péter_Máté | hasOccupation | singer |

# 2. Unmatched triples

**Total unmatched count: 19**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 19**

| Subject | Predicate | Object |
|---|---|---|
| Michael_D_Antonovich | type | Person |
| Michael_D_Antonovich | type | NamedIndividual |
| Michael_D_Antonovich | label | "Michael D. Antonovich" |
| Péter_Máté | type | Person |
| Péter_Máté | type | NamedIndividual |
| Péter_Máté | label | "Péter Máté (pop singer)" |
| Péter_Máté | altLabel | "Péter Máté" |
| composer | type | Occupation |
| composer | type | NamedIndividual |
| composer | label | "composer" |
| pianist | type | Occupation |
| pianist | type | NamedIndividual |
| pianist | label | "pianist" |
| politician | type | Occupation |
| politician | type | NamedIndividual |
| politician | label | "politician" |
| singer | type | Occupation |
| singer | type | NamedIndividual |
| singer | label | "pop singer" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 23 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 23 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 19 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.173913 |
| Recall | 1.000000 |
| F1 score | 0.296296 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
