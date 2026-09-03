# Triple matching report: 622

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| CRD | hasDirector | Kranti_Kanade |
| Kranti_Kanade | hasEducatedAt | UCLA |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| CRD | type | Film |
| CRD | type | NamedIndividual |
| CRD | label | "CRD" |
| Kranti_Kanade | hasEducatedAt | edu_ftii |
| Kranti_Kanade | type | Person |
| Kranti_Kanade | type | NamedIndividual |
| Kranti_Kanade | label | "Kranti Kanade" |
| UCLA | type | EducationalInstitution |
| UCLA | type | NamedIndividual |
| UCLA | label | "University of California, Los Angeles" |
| UCLA | altLabel | "UCLA" |
| edu_ftii | type | EducationalInstitution |
| edu_ftii | type | NamedIndividual |
| edu_ftii | label | "Film and Television Institute of India" |
| edu_ftii | altLabel | "FTII" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.117647 |
| Recall | 1.000000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
