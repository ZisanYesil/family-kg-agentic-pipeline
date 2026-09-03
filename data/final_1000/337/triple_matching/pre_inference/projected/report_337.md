# Triple matching report: 337

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Andrew_Montagu_Douglas_Scott | hasParent | Louisa_Jane_Hamilton |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louisa_Jane_Montagu_Douglas_Scott_Duchess_of_Buccleuch | hasParent | James_Hamilton |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Andrew_Montagu_Douglas_Scott | type | Person |
| Herbert_Andrew_Montagu_Douglas_Scott | type | NamedIndividual |
| Herbert_Andrew_Montagu_Douglas_Scott | label | "Lord Herbert Andrew Montagu Douglas Scott" |
| James_Hamilton | type | Person |
| James_Hamilton | type | NamedIndividual |
| James_Hamilton | label | "James Hamilton, 1st Duke of Abercorn" |
| Louisa_Jane_Hamilton | hasParent | James_Hamilton |
| Louisa_Jane_Hamilton | type | Person |
| Louisa_Jane_Hamilton | type | NamedIndividual |
| Louisa_Jane_Hamilton | label | "Lady Louisa Jane Hamilton" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
