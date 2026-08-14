# Triple matching report: 3

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Q4968933 | hasBirthDate | "1946-06-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q4968933 | hasChild | Q4969243 |
| Q4968933 | type | Agent |
| Q4968933 | type | Person |
| Q4969243 | hasFather | Q4968933 |
| Q4969243 | hasParent | Q4968933 |
| Q4969243 | type | Agent |
| Q4969243 | type | Person |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Q4969243 | hasBirthDate | "1975-09-14"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 9 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.888889 |
| Recall | 1.000000 |
| F1 score | 0.941176 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
