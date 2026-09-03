# Triple matching report: 124

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Boulton_Watt | hasFounder | Matthew_Boulton |
| Matthew_Boulton | hasDeathDate | "1809-08-17"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Boulton_Watt | hasFounder | james_watt_1736 |
| Boulton_Watt | type | Organization |
| Boulton_Watt | type | NamedIndividual |
| Boulton_Watt | label | "Boulton & Watt" |
| Boulton_Watt | altLabel | "Boulton and Watt" |
| Matthew_Boulton | type | Person |
| Matthew_Boulton | type | NamedIndividual |
| Matthew_Boulton | label | "Matthew Boulton" |
| james_watt_1736 | hasDeathDate | "1819-08-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| james_watt_1736 | type | Person |
| james_watt_1736 | type | NamedIndividual |
| james_watt_1736 | label | "James Watt" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
