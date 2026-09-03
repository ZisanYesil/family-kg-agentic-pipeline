# Triple matching report: 222

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Giacomo_Cimini | hasEducatedAt | London_Film_School |
| Red_Riding_Hood | hasDirector | Giacomo_Cimini |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Giacomo_Cimini | type | Person |
| Giacomo_Cimini | type | NamedIndividual |
| Giacomo_Cimini | label | "Giacomo Cimini" |
| London_Film_School | type | EducationalInstitution |
| London_Film_School | type | NamedIndividual |
| London_Film_School | label | "London Film School" |
| Red_Riding_Hood | type | Film |
| Red_Riding_Hood | type | NamedIndividual |
| Red_Riding_Hood | label | "Red Riding Hood (2003 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
