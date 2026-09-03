# Triple matching report: 632

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Austria | type | Country |
| Austria | type | Place |
| Carnic_Alps | hasCountry | Austria |
| Carnic_Alps | hasCountry | Italy |
| Italy | type | Country |
| Italy | type | Place |
| Torre_del_Gran_San_Pietro | hasCountry | Italy |

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
| Carnic_Alps | type | Place |
| Torre_del_Gran_San_Pietro | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 9 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.777778 |
| Recall | 1.000000 |
| F1 score | 0.875000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
