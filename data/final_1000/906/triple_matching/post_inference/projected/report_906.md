# Triple matching report: 906

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| George_of_Lencastre_2nd_Duke_of_Aveiro | hasParent | John_of_Lencastre_1st_Duke_of_Aveiro |
| George_of_Lencastre_2nd_Duke_of_Aveiro | type | Agent |
| George_of_Lencastre_2nd_Duke_of_Aveiro | type | Person |
| John_of_Lencastre_1st_Duke_of_Aveiro | hasChild | George_of_Lencastre_2nd_Duke_of_Aveiro |
| John_of_Lencastre_1st_Duke_of_Aveiro | type | Agent |
| John_of_Lencastre_1st_Duke_of_Aveiro | type | Person |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| John_of_Lencastre_1st_Duke_of_Aveiro | hasBirthDate | "1501"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 7 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 1 |
| Precision | 1.000000 |
| Recall | 0.857143 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
