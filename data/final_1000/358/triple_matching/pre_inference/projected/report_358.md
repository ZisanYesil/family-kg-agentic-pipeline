# Triple matching report: 358

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Andrzeja_Górska | hasBirthDate | "1917-02-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Andrzeja_Górska | hasDeathDate | "2007-12-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Chilton | hasBirthDate | "1932-07-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Chilton | hasDeathDate | "2016-02-25"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Andrzeja_Górska | type | Person |
| Andrzeja_Górska | type | NamedIndividual |
| Andrzeja_Górska | label | "Andrzeja Górska" |
| Andrzeja_Górska | altLabel | "Andrzeja Górska" |
| Andrzeja_Górska | altLabel | "Maria Stefania Górska" |
| John_Chilton | type | Person |
| John_Chilton | type | NamedIndividual |
| John_Chilton | label | "John Chilton" |
| John_Chilton | altLabel | "John Chilton" |
| John_Chilton | altLabel | "John James Chilton" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 14 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.285714 |
| Recall | 1.000000 |
| F1 score | 0.444444 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
