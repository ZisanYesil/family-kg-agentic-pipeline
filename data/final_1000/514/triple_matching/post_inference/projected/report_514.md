# Triple matching report: 514

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Anna_of_Saxony | hasBirthDate | "1544-12-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Anna_of_Saxony | hasChild | Countess_Anna_of_Nassau |
| Anna_of_Saxony | type | Agent |
| Anna_of_Saxony | type | Person |
| Countess_Anna_of_Nassau | hasParent | Anna_of_Saxony |
| Countess_Anna_of_Nassau | type | Agent |
| Countess_Anna_of_Nassau | type | Person |

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
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 7 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 0 |
| Precision | 1.000000 |
| Recall | 1.000000 |
| F1 score | 1.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
