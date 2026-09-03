# Triple matching report: 412

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Clarice_Orsini | hasSpouse | Lorenzo_de_Medici |
| Clarice_Orsini | type | Agent |
| Clarice_Orsini | type | Person |
| Lorenzo_de_Medici | hasSpouse | Clarice_Orsini |
| Lorenzo_de_Medici | type | Agent |
| Lorenzo_de_Medici | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Florentine_Republic | type | Country |
| Florentine_Republic | type | Place |
| Lorenzo_de_Medici | hasCountry | Florentine_Republic |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Lorenzo_de_Medici | hasCountry | italy |
| italy | type | Country |
| italy | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.666667 |
| Recall | 0.666667 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
