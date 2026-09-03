# Triple matching report: 3

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Jean_Martin | hasSpouse | William_Black |
| Jean_Martin | type | Agent |
| Jean_Martin | type | Person |
| William_Black | hasDeathDate | "1983"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| William_Black | hasSpouse | Jean_Martin |
| William_Black | type | Agent |
| William_Black | type | Person |

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
