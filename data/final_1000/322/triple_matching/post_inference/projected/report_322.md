# Triple matching report: 322

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| All_American_Co_ed | type | Artifact |
| All_American_Co_ed | type | CreativeWork |
| Djamaluddin_Malik | hasBirthDate | "1917-02-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Djamaluddin_Malik | type | Agent |
| Djamaluddin_Malik | type | Person |
| Lagu_Kenangan | hasProducer | Djamaluddin_Malik |
| Lagu_Kenangan | type | Artifact |
| Lagu_Kenangan | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| All_American_Co_ed | hasProducer | Hal_Roach |
| Hal_Roach | hasBirthDate | "1892-01-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hal_Roach | type | Agent |
| Hal_Roach | type | Person |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| All_American_Co_ed | hasProducer | leroy_prinz |
| All_American_Co_ed | type | Film |
| Lagu_Kenangan | type | Film |
| leroy_prinz | type | Agent |
| leroy_prinz | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 17 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.615385 |
| Recall | 0.666667 |
| F1 score | 0.640000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
