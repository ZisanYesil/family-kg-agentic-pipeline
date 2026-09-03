# Triple matching report: 430

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| England | type | Country |
| England | type | Place |
| Ordgar | hasChild | Ordwulf |
| Ordgar | type | Agent |
| Ordgar | type | Person |
| Ordwulf | hasParent | Ordgar |
| Ordwulf | type | Agent |
| Ordwulf | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Ordgar_Ealdorman_of_Devon | hasCountry | England |
| Ordgar_Ealdorman_of_Devon | type | Agent |
| Ordgar_Ealdorman_of_Devon | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Ordgar | hasCountry | England |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.888889 |
| Recall | 0.727273 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
