# Triple matching report: 855

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Condemned_Women | hasCreator | Lew_Landers |
| Condemned_Women | hasDirector | Lew_Landers |
| Condemned_Women | type | Artifact |
| Condemned_Women | type | CreativeWork |
| Condemned_Women | type | Film |
| David_Eady | type | Agent |
| David_Eady | type | Person |
| Faces_in_the_Dark | hasCreator | David_Eady |
| Faces_in_the_Dark | hasDirector | David_Eady |
| Faces_in_the_Dark | type | Artifact |
| Faces_in_the_Dark | type | CreativeWork |
| Faces_in_the_Dark | type | Film |
| Lew_Landers | hasDeathDate | "1962-12-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lew_Landers | type | Agent |
| Lew_Landers | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| David_Eady_film_director | hasDeathDate | "2009-04-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Eady_film_director | type | Agent |
| David_Eady_film_director | type | Person |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| David_Eady | hasBirthDate | "1924-04-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Eady | hasDeathDate | "2009-04-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lew_Landers | hasBirthDate | "1901-01-02"^^<http://www.w3.org/2001/XMLSchema#date> |

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
