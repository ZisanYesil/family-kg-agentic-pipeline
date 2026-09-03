# Triple matching report: 948

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Calling_Philo_Vance | hasDirector | William_Clemens |
| Riccardo_Freda | hasDeathDate | "1999-12-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Witch_s_Curse | hasDirector | Riccardo_Freda |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| William_Clemens_film_director | hasDeathDate | "1980-04-29"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Calling_Philo_Vance | type | Film |
| Calling_Philo_Vance | type | NamedIndividual |
| Calling_Philo_Vance | label | "Calling Philo Vance" |
| Calling_Philo_Vance | altLabel | "Calling Philo Vance" |
| Riccardo_Freda | type | Person |
| Riccardo_Freda | type | NamedIndividual |
| Riccardo_Freda | label | "Riccardo Freda" |
| Riccardo_Freda | altLabel | "Riccardo Freda" |
| The_Witch_s_Curse | type | Film |
| The_Witch_s_Curse | type | NamedIndividual |
| The_Witch_s_Curse | label | "The Witch's Curse" |
| The_Witch_s_Curse | altLabel | "The Witch's Curse" |
| William_Clemens | hasDeathDate | "1980-04-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Clemens | type | Person |
| William_Clemens | type | NamedIndividual |
| William_Clemens | label | "William Clemens" |
| William_Clemens | altLabel | "William Clemens" |

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
