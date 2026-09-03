# Triple matching report: 972

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Everything_s_Ducky | hasDirector | Don_Taylor |
| Karthika_film | hasDirector | M_Krishnan_Nair |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Don_Taylor_American_actor_and_director | hasDeathDate | "1998-12-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair_director | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Don_Taylor | hasDeathDate | "1998-12-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Don_Taylor | type | Person |
| Don_Taylor | type | NamedIndividual |
| Don_Taylor | label | "Don Taylor" |
| Everything_s_Ducky | type | Film |
| Everything_s_Ducky | type | NamedIndividual |
| Everything_s_Ducky | label | "Everything's Ducky" |
| Karthika_film | type | Film |
| Karthika_film | type | NamedIndividual |
| Karthika_film | label | "Karthika" |
| M_Krishnan_Nair | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair | type | Person |
| M_Krishnan_Nair | type | NamedIndividual |
| M_Krishnan_Nair | label | "M. Krishnan Nair" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
