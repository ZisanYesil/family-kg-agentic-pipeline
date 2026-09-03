# Triple matching report: 322

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Djamaluddin_Malik | hasBirthDate | "1917-02-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lagu_Kenangan | hasProducer | Djamaluddin_Malik |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| All_American_Co_ed | hasProducer | Hal_Roach |
| Hal_Roach | hasBirthDate | "1892-01-14"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| All_American_Co_ed | hasProducer | leroy_prinz |
| All_American_Co_ed | type | Film |
| All_American_Co_ed | type | NamedIndividual |
| All_American_Co_ed | label | "All-American Co-ed" |
| Djamaluddin_Malik | type | Person |
| Djamaluddin_Malik | type | NamedIndividual |
| Djamaluddin_Malik | label | "Djamaluddin Malik" |
| Lagu_Kenangan | type | Film |
| Lagu_Kenangan | type | NamedIndividual |
| Lagu_Kenangan | label | "Lagu Kenangan" |
| leroy_prinz | type | Person |
| leroy_prinz | type | NamedIndividual |
| leroy_prinz | label | "Leroy Prinz" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.133333 |
| Recall | 0.500000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
