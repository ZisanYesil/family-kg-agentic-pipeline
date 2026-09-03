# Triple matching report: 344

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Henry_Strutt_2nd_Baron_Belper | hasBirthDate | "1840-05-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henry_Strutt_2nd_Baron_Belper | hasDeathDate | "1914-07-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nina_Škottová | hasBirthDate | "1946-10-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nina_Škottová | hasDeathDate | "2018-04-28"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Henry_Strutt_2nd_Baron_Belper | type | Person |
| Henry_Strutt_2nd_Baron_Belper | type | NamedIndividual |
| Henry_Strutt_2nd_Baron_Belper | label | "Henry Strutt, 2nd Baron Belper" |
| Nina_Škottová | type | Person |
| Nina_Škottová | type | NamedIndividual |
| Nina_Škottová | label | "Nina Škottová" |

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
