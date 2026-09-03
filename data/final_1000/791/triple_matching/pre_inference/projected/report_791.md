# Triple matching report: 791

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Louis_B_Mayer | hasDeathDate | "1957-10-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Famous_Mrs_Fair | hasProducer | Louis_B_Mayer |
| The_Flame_Barrier | hasProducer | Arthur_Gardner |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Gardner_producer | hasDeathDate | "2014-12-19"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Gardner | hasBirthDate | "1910-06-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Gardner | hasDeathDate | "2014-12-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Gardner | type | Person |
| Arthur_Gardner | type | NamedIndividual |
| Arthur_Gardner | label | "Arthur Gardner" |
| Louis_B_Mayer | hasBirthDate | "1884-07-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| Louis_B_Mayer | type | Person |
| Louis_B_Mayer | type | NamedIndividual |
| Louis_B_Mayer | label | "Louis B. Mayer" |
| The_Famous_Mrs_Fair | type | Film |
| The_Famous_Mrs_Fair | type | NamedIndividual |
| The_Famous_Mrs_Fair | label | "The Famous Mrs. Fair" |
| The_Flame_Barrier | type | Film |
| The_Flame_Barrier | type | NamedIndividual |
| The_Flame_Barrier | label | "The Flame Barrier" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 19 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.166667 |
| Recall | 0.750000 |
| F1 score | 0.272727 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
