# Triple matching report: 972

# 1. Matched triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Don_Taylor | type | Agent |
| Don_Taylor | type | Person |
| Everything_s_Ducky | hasCreator | Don_Taylor |
| Everything_s_Ducky | hasDirector | Don_Taylor |
| Everything_s_Ducky | type | Artifact |
| Everything_s_Ducky | type | CreativeWork |
| Everything_s_Ducky | type | Film |
| Karthika_film | hasCreator | M_Krishnan_Nair |
| Karthika_film | hasDirector | M_Krishnan_Nair |
| Karthika_film | type | Artifact |
| Karthika_film | type | CreativeWork |
| Karthika_film | type | Film |
| M_Krishnan_Nair | type | Agent |
| M_Krishnan_Nair | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Don_Taylor_American_actor_and_director | hasDeathDate | "1998-12-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Don_Taylor_American_actor_and_director | type | Agent |
| Don_Taylor_American_actor_and_director | type | Person |
| M_Krishnan_Nair_director | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair_director | type | Agent |
| M_Krishnan_Nair_director | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Don_Taylor | hasDeathDate | "1998-12-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| M_Krishnan_Nair | hasDeathDate | "2001-05-10"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 22 |
| True positives (matched) | 14 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.875000 |
| Recall | 0.700000 |
| F1 score | 0.777778 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
