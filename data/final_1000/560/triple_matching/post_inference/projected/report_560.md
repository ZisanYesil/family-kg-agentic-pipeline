# Triple matching report: 560

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gregorio_López_Raimundo | type | Agent |
| Gregorio_López_Raimundo | type | Person |
| Teresa_Pàmies_i_Bertran | type | Agent |
| Teresa_Pàmies_i_Bertran | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Gregorio_López_Raimundo | hasChild | Sergi_Pàmies |
| Sergi_Pàmies | hasParent | Gregorio_López_Raimundo |
| Sergi_Pàmies | hasParent | Teresa_Pàmies_i_Bertran |
| Sergi_Pàmies | type | Agent |
| Sergi_Pàmies | type | Person |
| Teresa_Pàmies_i_Bertran | hasChild | Sergi_Pàmies |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gregorio_López_Raimundo | hasSpouse | Teresa_Pàmies_i_Bertran |
| Teresa_Pàmies_i_Bertran | hasSpouse | Gregorio_López_Raimundo |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.666667 |
| Recall | 0.400000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
