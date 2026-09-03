# Triple matching report: 283

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Madeleine_Frieden_Kinnen | hasSpouse | Pierre_Frieden |
| Pierre_Frieden | hasDeathPlace | Zürich |

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
| Madeleine_Frieden_Kinnen | type | Person |
| Madeleine_Frieden_Kinnen | type | NamedIndividual |
| Madeleine_Frieden_Kinnen | label | "Madeleine Frieden-Kinnen" |
| Pierre_Frieden | type | Person |
| Pierre_Frieden | type | NamedIndividual |
| Pierre_Frieden | label | "Pierre Frieden" |
| Zürich | type | Place |
| Zürich | type | NamedIndividual |
| Zürich | label | "Zürich" |

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
