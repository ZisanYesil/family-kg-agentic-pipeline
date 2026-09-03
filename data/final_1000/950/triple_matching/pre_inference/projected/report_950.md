# Triple matching report: 950

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Fame_1936_film | hasDirector | Leslie_S_Hiscott |
| It_s_All_About_Love | hasDirector | Thomas_Vinterberg |
| Leslie_S_Hiscott | hasBirthDate | "1894-07-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Thomas_Vinterberg | hasBirthDate | "1969-05-19"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Fame_1936_film | type | Film |
| Fame_1936_film | type | NamedIndividual |
| Fame_1936_film | label | "Fame (1936 film)" |
| It_s_All_About_Love | type | Film |
| It_s_All_About_Love | type | NamedIndividual |
| It_s_All_About_Love | label | "It's All About Love" |
| Leslie_S_Hiscott | hasDeathDate | "1968-05-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Leslie_S_Hiscott | type | Person |
| Leslie_S_Hiscott | type | NamedIndividual |
| Leslie_S_Hiscott | label | "Leslie S. Hiscott" |
| Leslie_S_Hiscott | altLabel | "Leslie Stephenson Hiscott" |
| Thomas_Vinterberg | type | Person |
| Thomas_Vinterberg | type | NamedIndividual |
| Thomas_Vinterberg | label | "Thomas Vinterberg" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
