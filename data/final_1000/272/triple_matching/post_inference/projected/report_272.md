# Triple matching report: 272

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Adam_Osborne | type | Agent |
| Adam_Osborne | type | Person |
| Osborne_Computer_Corporation | hasFounder | Adam_Osborne |
| Osborne_Computer_Corporation | type | Agent |
| Osborne_Computer_Corporation | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Adam_Osborne | hasCountry | American |
| American | type | Country |
| American | type | Place |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| thailand | type | Country |
| thailand | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.714286 |
| Recall | 0.625000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
