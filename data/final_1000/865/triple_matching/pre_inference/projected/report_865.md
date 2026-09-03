# Triple matching report: 865

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fernando_Cortés | hasSpouse | Mapy_Cortés |
| My_Three_Merry_Widows | hasDirector | Fernando_Cortés |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Fernando_Cortés | hasBirthDate | "1909-10-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Fernando_Cortés | hasDeathDate | "1979"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Fernando_Cortés | type | Person |
| Fernando_Cortés | type | NamedIndividual |
| Fernando_Cortés | label | "Fernando Cortés" |
| Mapy_Cortés | type | Person |
| Mapy_Cortés | type | NamedIndividual |
| Mapy_Cortés | label | "María del Pilar Cordero" |
| Mapy_Cortés | altLabel | "Mapy Cortés" |
| My_Three_Merry_Widows | type | Film |
| My_Three_Merry_Widows | type | NamedIndividual |
| My_Three_Merry_Widows | label | "My Three Merry Widows" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
