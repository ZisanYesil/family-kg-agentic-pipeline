# Triple matching report: 913

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Corridors_of_Blood | hasDirector | Robert_Day |
| Min_Marion | hasDirector | Nils_R_Müller |
| Nils_R_Müller | hasBirthDate | "1921-01-17"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Robert_Day_director | hasBirthDate | "1922-09-11"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Corridors_of_Blood | type | Film |
| Corridors_of_Blood | type | NamedIndividual |
| Corridors_of_Blood | label | "Corridors of Blood" |
| Min_Marion | hasPublicationDate | "1975"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Min_Marion | type | Film |
| Min_Marion | type | NamedIndividual |
| Min_Marion | label | "Min Marion" |
| Nils_R_Müller | hasDeathDate | "2007-03-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nils_R_Müller | type | Person |
| Nils_R_Müller | type | NamedIndividual |
| Nils_R_Müller | label | "Nils R. Müller" |
| Robert_Day | hasBirthDate | "1922-09-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Day | hasDeathDate | "2017-03-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Day | type | Person |
| Robert_Day | type | NamedIndividual |
| Robert_Day | label | "Robert Day" |
| Robert_Day | altLabel | "Robert Frederick Day" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.150000 |
| Recall | 0.750000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
