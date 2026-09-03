# Triple matching report: 58

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Andrzej_Markowski | hasBirthDate | "1924-08-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Andrzej_Markowski | hasDeathDate | "1986-10-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| François_Missoffe | hasBirthDate | "1919-10-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| François_Missoffe | hasDeathDate | "2003-08-28"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Andrzej_Markowski | type | Person |
| Andrzej_Markowski | type | NamedIndividual |
| Andrzej_Markowski | label | "Andrzej Markowski" |
| François_Missoffe | type | Person |
| François_Missoffe | type | NamedIndividual |
| François_Missoffe | label | "François Missoffe" |

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
