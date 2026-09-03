# Triple matching report: 337

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Andrew_Montagu_Douglas_Scott | hasParent | Louisa_Jane_Hamilton |
| Herbert_Andrew_Montagu_Douglas_Scott | type | Agent |
| Herbert_Andrew_Montagu_Douglas_Scott | type | Person |
| James_Hamilton | type | Agent |
| James_Hamilton | type | Person |
| Louisa_Jane_Hamilton | hasChild | Herbert_Andrew_Montagu_Douglas_Scott |
| Louisa_Jane_Hamilton | type | Agent |
| Louisa_Jane_Hamilton | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| James_Hamilton | hasChild | Louisa_Jane_Montagu_Douglas_Scott_Duchess_of_Buccleuch |
| Louisa_Jane_Montagu_Douglas_Scott_Duchess_of_Buccleuch | hasParent | James_Hamilton |
| Louisa_Jane_Montagu_Douglas_Scott_Duchess_of_Buccleuch | type | Agent |
| Louisa_Jane_Montagu_Douglas_Scott_Duchess_of_Buccleuch | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| James_Hamilton | hasChild | Louisa_Jane_Hamilton |
| Louisa_Jane_Hamilton | hasParent | James_Hamilton |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.800000 |
| Recall | 0.666667 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
