# Triple matching report: 999

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Collector_Malathy | hasCreator | M_Krishnan_Nair |
| Collector_Malathy | hasDirector | M_Krishnan_Nair |
| Collector_Malathy | type | Artifact |
| Collector_Malathy | type | CreativeWork |
| Collector_Malathy | type | Film |
| John_Brahm | hasDeathDate | "1982-10-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Brahm | type | Agent |
| John_Brahm | type | Person |
| M_Krishnan_Nair | type | Agent |
| M_Krishnan_Nair | type | Person |
| The_Locket | hasCreator | John_Brahm |
| The_Locket | hasDirector | John_Brahm |
| The_Locket | type | Artifact |
| The_Locket | type | CreativeWork |
| The_Locket | type | Film |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| M_Krishnan_Nair_director | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair_director | type | Agent |
| M_Krishnan_Nair_director | type | Person |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| John_Brahm | hasBirthDate | "1893-08-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair | hasBirthDate | "1926-11-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 21 |
| True positives (matched) | 15 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.833333 |
| Recall | 0.833333 |
| F1 score | 0.833333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
