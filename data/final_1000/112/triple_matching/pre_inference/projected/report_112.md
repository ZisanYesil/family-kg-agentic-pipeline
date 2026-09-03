# Triple matching report: 112

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Crockett_Johnson | hasBirthDate | "1906-10-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Crockett_Johnson | hasDeathDate | "1975-07-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sven_Olof_Lundgren | hasBirthDate | "1908-11-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sven_Olof_Lundgren | hasDeathDate | "1946-03-26"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Crockett_Johnson | type | Person |
| Crockett_Johnson | type | NamedIndividual |
| Crockett_Johnson | label | "Crockett Johnson" |
| Crockett_Johnson | altLabel | "David Johnson Leisk" |
| Sven_Olof_Lundgren | type | Person |
| Sven_Olof_Lundgren | type | NamedIndividual |
| Sven_Olof_Lundgren | label | "Sven-Olof Lundgren" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
