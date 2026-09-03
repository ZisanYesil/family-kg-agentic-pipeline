# Triple matching report: 957

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Frank_McDonald | type | Agent |
| Frank_McDonald | type | Person |
| George_Sherman | hasBirthDate | "1908-07-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_Sherman | type | Agent |
| George_Sherman | type | Person |
| Song_of_Arizona | hasCreator | Frank_McDonald |
| Song_of_Arizona | hasDirector | Frank_McDonald |
| Song_of_Arizona | type | Artifact |
| Song_of_Arizona | type | CreativeWork |
| Song_of_Arizona | type | Film |
| Texas_Terrors | hasCreator | George_Sherman |
| Texas_Terrors | hasDirector | George_Sherman |
| Texas_Terrors | type | Artifact |
| Texas_Terrors | type | CreativeWork |
| Texas_Terrors | type | Film |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Frank_McDonald_director | hasBirthDate | "1899-11-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Frank_McDonald_director | type | Agent |
| Frank_McDonald_director | type | Person |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Frank_McDonald | hasBirthDate | "1899-11-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Frank_McDonald | hasDeathDate | "1980-03-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_Sherman | hasDeathDate | "1991-03-15"^^<http://www.w3.org/2001/XMLSchema#date> |

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
