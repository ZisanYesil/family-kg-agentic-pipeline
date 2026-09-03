# Triple matching report: 491

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Franklin_Edson | hasBirthDate | "1832-04-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Franklin_Edson | hasDeathDate | "1904-09-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Martino_Finotto | hasBirthDate | "1933-11-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Martino_Finotto | hasDeathDate | "2014-08-13"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Franklin_Edson | type | Person |
| Franklin_Edson | type | NamedIndividual |
| Franklin_Edson | label | "Franklin Edson" |
| Martino_Finotto | type | Person |
| Martino_Finotto | type | NamedIndividual |
| Martino_Finotto | label | "Martino Finotto" |

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
