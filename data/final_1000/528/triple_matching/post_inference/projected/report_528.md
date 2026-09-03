# Triple matching report: 528

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| English | type | Country |
| English | type | Place |
| Sir_Edward_Acton_3rd_Baronet | hasParent | Sir_Walter_Acton_2nd_Baronet |
| Sir_Edward_Acton_3rd_Baronet | type | Agent |
| Sir_Edward_Acton_3rd_Baronet | type | Person |
| Sir_Walter_Acton_2nd_Baronet | hasChild | Sir_Edward_Acton_3rd_Baronet |
| Sir_Walter_Acton_2nd_Baronet | type | Agent |
| Sir_Walter_Acton_2nd_Baronet | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Sir_Walter_Acton | hasCountry | English |
| Sir_Walter_Acton | type | Agent |
| Sir_Walter_Acton | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sir_Walter_Acton_2nd_Baronet | hasCountry | English |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.888889 |
| Recall | 0.727273 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
