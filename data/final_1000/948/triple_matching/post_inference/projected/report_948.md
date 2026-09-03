# Triple matching report: 948

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Calling_Philo_Vance | hasCreator | William_Clemens |
| Calling_Philo_Vance | hasDirector | William_Clemens |
| Calling_Philo_Vance | type | Artifact |
| Calling_Philo_Vance | type | CreativeWork |
| Calling_Philo_Vance | type | Film |
| Riccardo_Freda | hasDeathDate | "1999-12-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Riccardo_Freda | type | Agent |
| Riccardo_Freda | type | Person |
| The_Witch_s_Curse | hasCreator | Riccardo_Freda |
| The_Witch_s_Curse | hasDirector | Riccardo_Freda |
| The_Witch_s_Curse | type | Artifact |
| The_Witch_s_Curse | type | CreativeWork |
| The_Witch_s_Curse | type | Film |
| William_Clemens | type | Agent |
| William_Clemens | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| William_Clemens_film_director | hasDeathDate | "1980-04-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Clemens_film_director | type | Agent |
| William_Clemens_film_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| William_Clemens | hasDeathDate | "1980-04-29"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 19 |
| True positives (matched) | 15 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.937500 |
| Recall | 0.833333 |
| F1 score | 0.882353 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
