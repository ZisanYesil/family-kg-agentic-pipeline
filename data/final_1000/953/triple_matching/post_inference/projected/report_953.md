# Triple matching report: 953

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Hussain_Nizam_Shah_I | hasChild | Murtaza_Nizam_Shah_I |
| Hussain_Nizam_Shah_I | type | Agent |
| Hussain_Nizam_Shah_I | type | Person |
| Murtaza_Nizam_Shah_I | hasParent | Hussain_Nizam_Shah_I |
| Murtaza_Nizam_Shah_I | type | Agent |
| Murtaza_Nizam_Shah_I | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Ahmadnagar_Sultanate | type | Country |
| Ahmadnagar_Sultanate | type | Place |
| Hussain_Nizam_Shah_I | hasCountry | Ahmadnagar_Sultanate |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Hussain_Nizam_Shah_I | hasCountry | india |
| india | type | Country |
| india | type | Place |

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
