# Triple matching report: 482

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ludwig_Elsbett | hasBirthDate | "1913-11-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ludwig_Elsbett | hasDeathDate | "2003-03-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pamela_Ann_Rymer | hasBirthDate | "1941-01-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pamela_Ann_Rymer | hasDeathDate | "2011-09-21"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Ludwig_Elsbett | type | Person |
| Ludwig_Elsbett | type | NamedIndividual |
| Ludwig_Elsbett | label | "Ludwig Elsbett" |
| Pamela_Ann_Rymer | type | Person |
| Pamela_Ann_Rymer | type | NamedIndividual |
| Pamela_Ann_Rymer | label | "Pamela Ann Rymer" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
