# Triple matching report: 957

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| George_Sherman | hasBirthDate | "1908-07-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Song_of_Arizona | hasDirector | Frank_McDonald |
| Texas_Terrors | hasDirector | George_Sherman |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Frank_McDonald_director | hasBirthDate | "1899-11-09"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Frank_McDonald | hasBirthDate | "1899-11-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Frank_McDonald | hasDeathDate | "1980-03-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Frank_McDonald | type | Person |
| Frank_McDonald | type | NamedIndividual |
| Frank_McDonald | label | "Frank McDonald" |
| George_Sherman | hasDeathDate | "1991-03-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_Sherman | type | Person |
| George_Sherman | type | NamedIndividual |
| George_Sherman | label | "George Sherman" |
| Song_of_Arizona | type | Film |
| Song_of_Arizona | type | NamedIndividual |
| Song_of_Arizona | label | "Song of Arizona" |
| Texas_Terrors | type | Film |
| Texas_Terrors | type | NamedIndividual |
| Texas_Terrors | label | "Texas Terrors" |

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
