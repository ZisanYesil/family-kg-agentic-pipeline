# Triple matching report: 521

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| ULTRA_Diamonds | hasCountry | United_States |
| United_States | type | Country |
| United_States | type | Place |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Dillon_Dam_Brewery | hasCountry | U_S_A |
| U_S_A | type | Country |
| U_S_A | type | Place |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Dillon_Dam_Brewery | hasCountry | United_States |
| Dillon_Dam_Brewery | type | Agent |
| Dillon_Dam_Brewery | type | Organization |
| ULTRA_Diamonds | type | Agent |
| ULTRA_Diamonds | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 11 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.375000 |
| Recall | 0.500000 |
| F1 score | 0.428571 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
