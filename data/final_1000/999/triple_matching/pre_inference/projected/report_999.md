# Triple matching report: 999

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Collector_Malathy | hasDirector | M_Krishnan_Nair |
| John_Brahm | hasDeathDate | "1982-10-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Locket | hasDirector | John_Brahm |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| M_Krishnan_Nair_director | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Collector_Malathy | type | Film |
| Collector_Malathy | type | NamedIndividual |
| Collector_Malathy | label | "Collector Malathy" |
| John_Brahm | hasBirthDate | "1893-08-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Brahm | type | Person |
| John_Brahm | type | NamedIndividual |
| John_Brahm | label | "John Brahm" |
| M_Krishnan_Nair | hasBirthDate | "1926-11-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair | type | Person |
| M_Krishnan_Nair | type | NamedIndividual |
| M_Krishnan_Nair | label | "M. Krishnan Nair" |
| The_Locket | type | Film |
| The_Locket | type | NamedIndividual |
| The_Locket | label | "The Locket" |

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
