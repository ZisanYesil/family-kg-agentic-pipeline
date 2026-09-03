# Triple matching report: 642

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Lake_Powell | hasCountry | United_States |
| United_States | type | Country |
| United_States | type | Place |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Takhlakh_Lake | hasCountry | U_S |
| U_S | type | Country |
| U_S | type | Place |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Lake_Powell | type | Place |
| Takhlakh_Lake | hasCountry | United_States |
| Takhlakh_Lake | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 9 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.500000 |
| Recall | 0.500000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
