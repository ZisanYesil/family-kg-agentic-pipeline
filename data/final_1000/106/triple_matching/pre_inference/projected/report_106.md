# Triple matching report: 106

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Peder_Per_Veggum | hasBirthDate | "1768-04-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Peder_Per_Veggum | hasDeathDate | "1836-04-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Piero_Campelli | hasBirthDate | "1893-12-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Piero_Campelli | hasDeathDate | "1946-10-20"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Peder_Per_Veggum | type | Person |
| Peder_Per_Veggum | type | NamedIndividual |
| Peder_Per_Veggum | label | "Peder Per Veggum" |
| Piero_Campelli | type | Person |
| Piero_Campelli | type | NamedIndividual |
| Piero_Campelli | label | "Piero Campelli" |

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
