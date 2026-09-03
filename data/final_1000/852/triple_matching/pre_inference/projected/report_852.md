# Triple matching report: 852

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Coulson_Wallop | hasParent | John_Wallop_2nd_Earl_of_Portsmouth |
| John_Wallop_2nd_Earl_of_Portsmouth | hasEducatedAt | Oxford |

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
| Coulson_Wallop | type | Person |
| Coulson_Wallop | type | NamedIndividual |
| Coulson_Wallop | label | "Coulson Wallop" |
| John_Wallop_2nd_Earl_of_Portsmouth | type | Person |
| John_Wallop_2nd_Earl_of_Portsmouth | type | NamedIndividual |
| John_Wallop_2nd_Earl_of_Portsmouth | label | "John Wallop, 2nd Earl of Portsmouth" |
| Oxford | type | EducationalInstitution |
| Oxford | type | NamedIndividual |
| Oxford | label | "Oxford" |

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
