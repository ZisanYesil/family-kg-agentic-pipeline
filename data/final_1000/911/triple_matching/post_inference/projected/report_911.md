# Triple matching report: 911

# 1. Matched triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Amos_Gitai | hasBirthDate | "1950-10-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Amos_Gitai | type | Agent |
| Amos_Gitai | type | Person |
| Arthur_Maude | hasBirthDate | "1880-07-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Maude | type | Agent |
| Arthur_Maude | type | Person |
| Berlin_Jerusalem | hasCreator | Amos_Gitai |
| Berlin_Jerusalem | hasDirector | Amos_Gitai |
| Berlin_Jerusalem | type | Artifact |
| Berlin_Jerusalem | type | CreativeWork |
| Berlin_Jerusalem | type | Film |
| The_Shadow_of_Nazareth | hasCreator | Arthur_Maude |
| The_Shadow_of_Nazareth | hasDirector | Arthur_Maude |
| The_Shadow_of_Nazareth | type | Artifact |
| The_Shadow_of_Nazareth | type | CreativeWork |
| The_Shadow_of_Nazareth | type | Film |

# 2. Unmatched triples

**Total unmatched count: 0**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 16 |
| Union triples in scope | 16 |
| True positives (matched) | 16 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 0 |
| Precision | 1.000000 |
| Recall | 1.000000 |
| F1 score | 1.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
