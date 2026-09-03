# Triple matching report: 447

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Coretta_Scott_King | hasChild | Dexter_Scott_King |
| Coretta_Scott_King | type | Agent |
| Coretta_Scott_King | type | Person |
| Dexter_Scott_King | hasParent | Coretta_Scott_King |
| Dexter_Scott_King | type | Agent |
| Dexter_Scott_King | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Coretta_Scott_King | hasBurialPlace | Georgia |
| Georgia | type | Place |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Coretta_Scott_King | hasBurialPlace | king_center |
| king_center | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.750000 |
| Recall | 0.750000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
