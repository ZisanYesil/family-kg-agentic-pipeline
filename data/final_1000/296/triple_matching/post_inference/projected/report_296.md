# Triple matching report: 296

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Jan_Nepomucen_Potocki | hasParent | Stanisław_Antoni_Potocki |
| Jan_Nepomucen_Potocki | hasSpouse | Róża_Maria_Wodzicka |
| Jan_Nepomucen_Potocki | type | Agent |
| Jan_Nepomucen_Potocki | type | Person |
| Róża_Maria_Wodzicka | hasSpouse | Jan_Nepomucen_Potocki |
| Róża_Maria_Wodzicka | type | Agent |
| Róża_Maria_Wodzicka | type | Person |
| Stanisław_Antoni_Potocki | hasChild | Jan_Nepomucen_Potocki |
| Stanisław_Antoni_Potocki | type | Agent |
| Stanisław_Antoni_Potocki | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Jan_Nepomucen_Potocki | hasSpouse | maria_szajer |
| maria_szajer | hasSpouse | Jan_Nepomucen_Potocki |
| maria_szajer | type | Agent |
| maria_szajer | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.714286 |
| Recall | 1.000000 |
| F1 score | 0.833333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
