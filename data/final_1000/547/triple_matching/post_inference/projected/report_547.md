# Triple matching report: 547

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Bottle_Caps | hasManufacturer | Nestlé |
| Bottle_Caps | type | Artifact |
| Bottle_Caps | type | Product |
| Nestlé | hasCountry | Swiss |
| Nestlé | type | Agent |
| Swiss | type | Country |
| Swiss | type | Place |

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
| Nestlé | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.875000 |
| Recall | 1.000000 |
| F1 score | 0.933333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
