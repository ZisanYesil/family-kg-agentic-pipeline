# Triple matching report: 857

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Thietmar_Margrave_of_Meissen | hasDeathDate | "0979-08-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Thietmar_Margrave_of_Meissen | type | Agent |
| Thietmar_Margrave_of_Meissen | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gero_II_Margrave_of_the_Saxon_Ostmark | hasParent | Thietmar_Margrave_of_Meissen |
| Gero_II_Margrave_of_the_Saxon_Ostmark | type | Agent |
| Gero_II_Margrave_of_the_Saxon_Ostmark | type | Person |
| Thietmar_Margrave_of_Meissen | hasChild | Gero_II_Margrave_of_the_Saxon_Ostmark |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Thietmar_Margrave_of_Meissen | hasChild | gero_ii |
| gero_ii | hasParent | Thietmar_Margrave_of_Meissen |
| gero_ii | type | Agent |
| gero_ii | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 11 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.428571 |
| Recall | 0.428571 |
| F1 score | 0.428571 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
