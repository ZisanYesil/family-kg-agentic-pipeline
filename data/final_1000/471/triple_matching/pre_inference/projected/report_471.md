# Triple matching report: 471

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Edward_Bulstrode | hasEducatedAt | St_John_s_College |
| Richard_Bulstrode | hasParent | Edward_Bulstrode |

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
| Edward_Bulstrode | type | Person |
| Edward_Bulstrode | type | NamedIndividual |
| Edward_Bulstrode | label | "Edward Bulstrode" |
| Richard_Bulstrode | type | Person |
| Richard_Bulstrode | type | NamedIndividual |
| Richard_Bulstrode | label | "Richard Bulstrode" |
| St_John_s_College | type | EducationalInstitution |
| St_John_s_College | type | NamedIndividual |
| St_John_s_College | label | "St. John's College, Oxford" |

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
