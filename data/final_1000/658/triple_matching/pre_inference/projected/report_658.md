# Triple matching report: 658

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Next_List | hasPresenter | Sanjay_Gupta |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sanjay_Gupta | hasEmployer | Emory_University |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Sanjay_Gupta | hasEmployer | cnn |
| Sanjay_Gupta | type | Person |
| Sanjay_Gupta | type | NamedIndividual |
| Sanjay_Gupta | label | "Sanjay Gupta" |
| The_Next_List | type | CreativeWork |
| The_Next_List | type | NamedIndividual |
| The_Next_List | label | "The Next List" |
| cnn | type | Organization |
| cnn | type | NamedIndividual |
| cnn | label | "CNN" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
