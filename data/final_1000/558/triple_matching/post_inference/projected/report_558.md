# Triple matching report: 558

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Alice_of_Normandy | hasChild | William_I_Count_of_Burgundy |
| Alice_of_Normandy | type | Agent |
| Alice_of_Normandy | type | Person |
| Sybilla_of_Burgundy | hasParent | William_I_Count_of_Burgundy |
| Sybilla_of_Burgundy | type | Agent |
| Sybilla_of_Burgundy | type | Person |
| William_I_Count_of_Burgundy | hasChild | Sybilla_of_Burgundy |
| William_I_Count_of_Burgundy | hasParent | Alice_of_Normandy |
| William_I_Count_of_Burgundy | type | Agent |
| William_I_Count_of_Burgundy | type | Person |

# 2. Unmatched triples

**Total unmatched count: 0**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 10 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 0 |
| Precision | 1.000000 |
| Recall | 1.000000 |
| F1 score | 1.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
