# Triple matching report: 907

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Friedrich_Gottlob_Uhlemann | hasChild | Max_Uhlemann |
| Friedrich_Gottlob_Uhlemann | hasEmployer | University_of_Berlin |
| Friedrich_Gottlob_Uhlemann | type | Agent |
| Friedrich_Gottlob_Uhlemann | type | Person |
| Max_Uhlemann | hasParent | Friedrich_Gottlob_Uhlemann |
| Max_Uhlemann | type | Agent |
| Max_Uhlemann | type | Person |
| University_of_Berlin | type | Agent |
| University_of_Berlin | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Friedrich_Gottlob_Uhlemann | hasEmployer | university_of_leipzig |
| university_of_leipzig | type | Agent |
| university_of_leipzig | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
