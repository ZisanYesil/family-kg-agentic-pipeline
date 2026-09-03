# Triple matching report: 159

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Canada | type | Country |
| Canada | type | Place |
| Gordon_Bell_High_School | hasCountry | Canada |
| Polyvalente_W_A_Losier | hasCountry | Canada |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gordon_Bell_High_School | type | Agent |
| Gordon_Bell_High_School | type | Organization |
| Polyvalente_W_A_Losier | type | Agent |
| Polyvalente_W_A_Losier | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 8 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.500000 |
| Recall | 1.000000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
