# Triple matching report: 858

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| William_Douglas_2nd_Earl_of_Angus | hasBirthPlace | Tantallon_Castle |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| James_Douglas_3rd_Earl_of_Angus | hasParent | William_Douglas_2nd_Earl_of_Angus |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| James_Douglas_3rd_Earl_of_Angus | type | Person |
| James_Douglas_3rd_Earl_of_Angus | type | NamedIndividual |
| James_Douglas_3rd_Earl_of_Angus | label | "James Douglas, 3rd Earl of Angus" |
| Tantallon_Castle | type | Place |
| Tantallon_Castle | type | NamedIndividual |
| Tantallon_Castle | label | "Tantallon Castle" |
| William_Douglas_2nd_Earl_of_Angus | hasChild | James_Douglas_3rd_Earl_of_Angus |
| William_Douglas_2nd_Earl_of_Angus | type | Person |
| William_Douglas_2nd_Earl_of_Angus | type | NamedIndividual |
| William_Douglas_2nd_Earl_of_Angus | label | "William Douglas, 2nd Earl of Angus" |

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
