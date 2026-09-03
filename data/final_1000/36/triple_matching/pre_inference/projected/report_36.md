# Triple matching report: 36

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Benjamin_Nottingham_Webster | hasBirthDate | "1797-09-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Benjamin_Nottingham_Webster | hasDeathDate | "1882-07-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Huchtenburg | hasBirthDate | "1647-11-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Huchtenburg | hasDeathDate | "1733-07-02"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Benjamin_Nottingham_Webster | type | Person |
| Benjamin_Nottingham_Webster | type | NamedIndividual |
| Benjamin_Nottingham_Webster | label | "Benjamin Nottingham Webster" |
| Benjamin_Nottingham_Webster | altLabel | "Benjamin Nottingham Webster" |
| Huchtenburg | type | Person |
| Huchtenburg | type | NamedIndividual |
| Huchtenburg | label | "Jan van Huchtenburg" |
| Huchtenburg | altLabel | "Jan van Huchtenburg" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.333333 |
| Recall | 1.000000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
