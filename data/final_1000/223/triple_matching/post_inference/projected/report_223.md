# Triple matching report: 223

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Brazil | type | Country |
| Brazil | type | Place |
| Dos_Patos_River_Ivaí_River | hasCountry | Brazil |
| Jaguarizinho_River | hasCountry | Brazil |

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
| Dos_Patos_River_Ivaí_River | type | Place |
| Jaguarizinho_River | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 6 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.666667 |
| Recall | 1.000000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
