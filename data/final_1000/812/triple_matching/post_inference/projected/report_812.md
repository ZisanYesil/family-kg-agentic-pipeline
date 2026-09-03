# Triple matching report: 812

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| 24_Hour_Psycho | hasCreator | Douglas_Gordon |
| 24_Hour_Psycho | type | Artifact |
| 24_Hour_Psycho | type | CreativeWork |
| 24_Hour_Psycho | type | Film |
| Douglas_Gordon | hasAwardReceived | Turner_Prize |
| Douglas_Gordon | type | Agent |
| Douglas_Gordon | type | Person |
| Turner_Prize | type | Award |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| 24_Hour_Psycho | hasDirector | Douglas_Gordon |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 9 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 1 |
| Precision | 1.000000 |
| Recall | 0.888889 |
| F1 score | 0.941176 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
