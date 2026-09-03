# Triple matching report: 913

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Corridors_of_Blood | hasCreator | Robert_Day |
| Corridors_of_Blood | hasDirector | Robert_Day |
| Corridors_of_Blood | type | Artifact |
| Corridors_of_Blood | type | CreativeWork |
| Corridors_of_Blood | type | Film |
| Min_Marion | hasCreator | Nils_R_Müller |
| Min_Marion | hasDirector | Nils_R_Müller |
| Min_Marion | type | Artifact |
| Min_Marion | type | CreativeWork |
| Min_Marion | type | Film |
| Nils_R_Müller | hasBirthDate | "1921-01-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nils_R_Müller | type | Agent |
| Nils_R_Müller | type | Person |
| Robert_Day | type | Agent |
| Robert_Day | type | Person |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Robert_Day_director | hasBirthDate | "1922-09-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Day_director | type | Agent |
| Robert_Day_director | type | Person |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Min_Marion | hasPublicationDate | "1975"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Nils_R_Müller | hasDeathDate | "2007-03-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Day | hasBirthDate | "1922-09-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Day | hasDeathDate | "2017-03-17"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 22 |
| True positives (matched) | 15 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.789474 |
| Recall | 0.833333 |
| F1 score | 0.810811 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
