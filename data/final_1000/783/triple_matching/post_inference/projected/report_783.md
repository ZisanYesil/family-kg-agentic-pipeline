# Triple matching report: 783

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gianni_Versace | hasDeathPlace | Miami_Beach |
| Gianni_Versace | type | Agent |
| Gianni_Versace | type | Person |
| Miami_Beach | type | Place |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Versus | hasFounder | Gianni_Versace |
| Versus | type | Agent |
| Versus | type | Organization |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| versus_versace_artifact | type | Artifact |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 5 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.800000 |
| Recall | 0.571429 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
