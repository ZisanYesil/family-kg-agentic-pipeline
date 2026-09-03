# Triple matching report: 172

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Inthaphom | hasParent | Inthasom |
| Inthaphom | type | Agent |
| Inthaphom | type | Person |
| Inthasom | hasChild | Inthaphom |
| Inthasom | hasSibling | Kingkitsarat |
| Inthasom | type | Agent |
| Inthasom | type | Person |
| Kingkitsarat | hasSibling | Inthasom |
| Kingkitsarat | type | Agent |
| Kingkitsarat | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Inthaphom | hasDeathDate | "1776"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Inthasom | hasDeathDate | "1749"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.833333 |
| Recall | 1.000000 |
| F1 score | 0.909091 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
