# Triple matching report: 5

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Q3536748 | hasBirthDate | "1918-03-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q3536748 | type | Agent |
| Q3536748 | type | Person |

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
| Q3536748 | hasDeathDate | "2001-06-21"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 4 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 4 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
