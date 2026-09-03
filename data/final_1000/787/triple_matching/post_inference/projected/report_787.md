# Triple matching report: 787

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Canada | type | Country |
| Canada | type | Place |
| Devils_Lake_North_Dakota | hasCountry | U_S |
| McLeod_Lake_Alberta | hasCountry | Canada |
| U_S | type | Country |
| U_S | type | Place |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Devils_Lake_North_Dakota | type | Place |
| McLeod_Lake_Alberta | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
