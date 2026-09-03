# Triple matching report: 741

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

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Florentine | type | Place |
| Lorenzo_de_Medici | hasBirthPlace | Florentine |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.750000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
