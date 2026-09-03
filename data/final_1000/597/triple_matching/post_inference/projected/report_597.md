# Triple matching report: 597

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Closed_Doors_Village | hasPublicationDate | "2014"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Closed_Doors_Village | type | Artifact |
| Closed_Doors_Village | type | CreativeWork |
| Poor_Girls | hasPublicationDate | "1927"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Poor_Girls | type | Artifact |
| Poor_Girls | type | CreativeWork |

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
| Closed_Doors_Village | type | Film |
| Poor_Girls | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
