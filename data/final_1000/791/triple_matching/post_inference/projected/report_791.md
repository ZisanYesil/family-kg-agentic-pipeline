# Triple matching report: 791

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Gardner | type | Agent |
| Louis_B_Mayer | hasDeathDate | "1957-10-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Louis_B_Mayer | type | Agent |
| Louis_B_Mayer | type | Person |
| The_Famous_Mrs_Fair | hasProducer | Louis_B_Mayer |
| The_Famous_Mrs_Fair | type | Artifact |
| The_Famous_Mrs_Fair | type | CreativeWork |
| The_Flame_Barrier | hasProducer | Arthur_Gardner |
| The_Flame_Barrier | type | Artifact |
| The_Flame_Barrier | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Gardner_producer | hasDeathDate | "2014-12-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Gardner_producer | type | Agent |
| Arthur_Gardner_producer | type | Person |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Gardner | hasBirthDate | "1910-06-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Gardner | hasDeathDate | "2014-12-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Gardner | type | Person |
| Louis_B_Mayer | hasBirthDate | "1884-07-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Famous_Mrs_Fair | type | Film |
| The_Flame_Barrier | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 13 |
| Union triples in scope | 19 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.625000 |
| Recall | 0.769231 |
| F1 score | 0.689655 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
