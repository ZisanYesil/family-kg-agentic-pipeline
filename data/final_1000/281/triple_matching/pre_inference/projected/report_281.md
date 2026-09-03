# Triple matching report: 281

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Giles | hasEducatedAt | Charterhouse_School |
| Lionel_Giles | hasParent | Herbert_Giles |

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
| Charterhouse_School | type | EducationalInstitution |
| Charterhouse_School | type | NamedIndividual |
| Charterhouse_School | label | "Charterhouse School" |
| Herbert_Giles | type | Person |
| Herbert_Giles | type | NamedIndividual |
| Herbert_Giles | label | "Herbert Giles" |
| Lionel_Giles | type | Person |
| Lionel_Giles | type | NamedIndividual |
| Lionel_Giles | label | "Lionel Giles" |

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
