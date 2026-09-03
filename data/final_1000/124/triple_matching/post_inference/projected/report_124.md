# Triple matching report: 124

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Boulton_Watt | hasFounder | Matthew_Boulton |
| Boulton_Watt | type | Agent |
| Boulton_Watt | type | Organization |
| Matthew_Boulton | hasDeathDate | "1809-08-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Matthew_Boulton | type | Agent |
| Matthew_Boulton | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Boulton_Watt | hasFounder | james_watt_1736 |
| james_watt_1736 | hasDeathDate | "1819-08-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| james_watt_1736 | type | Agent |
| james_watt_1736 | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.600000 |
| Recall | 1.000000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
