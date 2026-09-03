# Triple matching report: 507

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Dawn_Fraser | hasOccupation | politician |
| Dawn_Fraser | hasOccupation | swimmer |
| Dawn_Fraser | type | Agent |
| Dawn_Fraser | type | Person |
| Dunois_Master | hasOccupation | manuscript_illuminator |
| Dunois_Master | type | Agent |
| Dunois_Master | type | Person |
| manuscript_illuminator | type | Occupation |
| politician | type | Occupation |
| swimmer | type | Occupation |

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
| Dawn_Fraser | hasBirthDate | "1937-09-04"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 11 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.909091 |
| Recall | 1.000000 |
| F1 score | 0.952381 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
