# Triple matching report: 857

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Thietmar_Margrave_of_Meissen | hasDeathDate | "0979-08-03"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gero_II_Margrave_of_the_Saxon_Ostmark | hasParent | Thietmar_Margrave_of_Meissen |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Thietmar_Margrave_of_Meissen | type | Person |
| Thietmar_Margrave_of_Meissen | type | NamedIndividual |
| Thietmar_Margrave_of_Meissen | label | "Thietmar" |
| gero_ii | hasParent | Thietmar_Margrave_of_Meissen |
| gero_ii | type | Person |
| gero_ii | type | NamedIndividual |
| gero_ii | label | "Gero II" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
