# Triple matching report: 522

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Denis_Sanders | hasEducatedAt | UCLA |
| Shock_Treatment | hasDirector | Denis_Sanders |

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
| Denis_Sanders | type | Person |
| Denis_Sanders | type | NamedIndividual |
| Denis_Sanders | label | "Denis Sanders" |
| Shock_Treatment | type | Film |
| Shock_Treatment | type | NamedIndividual |
| Shock_Treatment | label | "Shock Treatment (1964 film)" |
| UCLA | type | EducationalInstitution |
| UCLA | type | NamedIndividual |
| UCLA | label | "UCLA" |

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
