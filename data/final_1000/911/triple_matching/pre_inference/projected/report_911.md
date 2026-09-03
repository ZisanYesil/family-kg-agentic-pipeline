# Triple matching report: 911

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Amos_Gitai | hasBirthDate | "1950-10-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Maude | hasBirthDate | "1880-07-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Berlin_Jerusalem | hasDirector | Amos_Gitai |
| The_Shadow_of_Nazareth | hasDirector | Arthur_Maude |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Amos_Gitai | type | Person |
| Amos_Gitai | type | NamedIndividual |
| Amos_Gitai | label | "Amos Gitai" |
| Arthur_Maude | type | Person |
| Arthur_Maude | type | NamedIndividual |
| Arthur_Maude | label | "Arthur Maude" |
| Arthur_Maude | altLabel | "Arthur John Maude" |
| Berlin_Jerusalem | type | Film |
| Berlin_Jerusalem | type | NamedIndividual |
| Berlin_Jerusalem | label | "Berlin-Jerusalem" |
| The_Shadow_of_Nazareth | type | Film |
| The_Shadow_of_Nazareth | type | NamedIndividual |
| The_Shadow_of_Nazareth | label | "The Shadow of Nazareth" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 17 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.235294 |
| Recall | 1.000000 |
| F1 score | 0.380952 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
