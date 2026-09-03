# Triple matching report: 903

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Billy_Ray_Cyrus | hasChild | Miley_Cyrus |
| Billy_Ray_Cyrus | type | Agent |
| Billy_Ray_Cyrus | type | Person |
| Lighter | hasCreator | Miley_Cyrus |
| Lighter | hasPerformer | Miley_Cyrus |
| Lighter | type | Artifact |
| Lighter | type | CreativeWork |
| Miley_Cyrus | hasParent | Billy_Ray_Cyrus |
| Miley_Cyrus | type | Agent |
| Miley_Cyrus | type | Person |

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
| Lighter | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 11 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.909091 |
| Recall | 1.000000 |
| F1 score | 0.952381 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
