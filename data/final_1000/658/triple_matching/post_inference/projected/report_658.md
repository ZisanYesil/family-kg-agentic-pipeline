# Triple matching report: 658

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Sanjay_Gupta | type | Agent |
| Sanjay_Gupta | type | Person |
| The_Next_List | hasPresenter | Sanjay_Gupta |
| The_Next_List | type | Artifact |
| The_Next_List | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Emory_University | type | Agent |
| Emory_University | type | Organization |
| Sanjay_Gupta | hasEmployer | Emory_University |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Sanjay_Gupta | hasEmployer | cnn |
| cnn | type | Agent |
| cnn | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 11 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.625000 |
| Recall | 0.625000 |
| F1 score | 0.625000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
