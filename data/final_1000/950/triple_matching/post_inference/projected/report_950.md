# Triple matching report: 950

# 1. Matched triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Fame_1936_film | hasCreator | Leslie_S_Hiscott |
| Fame_1936_film | hasDirector | Leslie_S_Hiscott |
| Fame_1936_film | type | Artifact |
| Fame_1936_film | type | CreativeWork |
| Fame_1936_film | type | Film |
| It_s_All_About_Love | hasCreator | Thomas_Vinterberg |
| It_s_All_About_Love | hasDirector | Thomas_Vinterberg |
| It_s_All_About_Love | type | Artifact |
| It_s_All_About_Love | type | CreativeWork |
| It_s_All_About_Love | type | Film |
| Leslie_S_Hiscott | hasBirthDate | "1894-07-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Leslie_S_Hiscott | type | Agent |
| Leslie_S_Hiscott | type | Person |
| Thomas_Vinterberg | hasBirthDate | "1969-05-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Thomas_Vinterberg | type | Agent |
| Thomas_Vinterberg | type | Person |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Leslie_S_Hiscott | hasDeathDate | "1968-05-03"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 16 |
| Union triples in scope | 17 |
| True positives (matched) | 16 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.941176 |
| Recall | 1.000000 |
| F1 score | 0.969697 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
