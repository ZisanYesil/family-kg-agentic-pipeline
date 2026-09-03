# Triple matching report: 855

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Condemned_Women | hasDirector | Lew_Landers |
| Faces_in_the_Dark | hasDirector | David_Eady |
| Lew_Landers | hasDeathDate | "1962-12-16"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| David_Eady_film_director | hasDeathDate | "2009-04-05"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Condemned_Women | type | Film |
| Condemned_Women | type | NamedIndividual |
| Condemned_Women | label | "Condemned Women" |
| David_Eady | hasBirthDate | "1924-04-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Eady | hasDeathDate | "2009-04-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Eady | type | Person |
| David_Eady | type | NamedIndividual |
| David_Eady | label | "David Eady" |
| Faces_in_the_Dark | type | Film |
| Faces_in_the_Dark | type | NamedIndividual |
| Faces_in_the_Dark | label | "Faces in the Dark" |
| Lew_Landers | hasBirthDate | "1901-01-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lew_Landers | type | Person |
| Lew_Landers | type | NamedIndividual |
| Lew_Landers | label | "Lew Landers" |
| Lew_Landers | altLabel | "Louis Friedlander" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.157895 |
| Recall | 0.750000 |
| F1 score | 0.260870 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
