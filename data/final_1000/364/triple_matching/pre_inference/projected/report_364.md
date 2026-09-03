# Triple matching report: 364

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Ruskin | hasBirthDate | "1924-04-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Joseph_Ruskin | hasDeathDate | "2013-12-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nicolae_Colan | hasBirthDate | "1893-11-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nicolae_Colan | hasDeathDate | "1967-04-15"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Joseph_Ruskin | type | Person |
| Joseph_Ruskin | type | NamedIndividual |
| Joseph_Ruskin | label | "Joseph Ruskin" |
| Nicolae_Colan | type | Person |
| Nicolae_Colan | type | NamedIndividual |
| Nicolae_Colan | label | "Nicolae Colan" |

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
