# Triple matching report: 115

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Arbusto_Energy | type | Agent |
| Arbusto_Energy | type | Organization |
| George_W_Bush | hasCountry | American |
| George_W_Bush | type | Agent |
| George_W_Bush | type | Person |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Arbusto_Energy | hasFounder | President_George_W_Bush |
| President_George_W_Bush | type | Agent |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Arbusto_Energy | hasFounder | George_W_Bush |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 10 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.875000 |
| Recall | 0.777778 |
| F1 score | 0.823529 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
