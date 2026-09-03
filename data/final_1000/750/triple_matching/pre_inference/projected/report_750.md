# Triple matching report: 750

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Georges_Lautner | hasParent | Renée_Saint_Cyr |
| La_Cage_aux_Folles_3_The_Wedding | hasDirector | Georges_Lautner |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Georges_Lautner | hasBirthDate | "1926-01-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Georges_Lautner | hasDeathDate | "2013-11-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Georges_Lautner | type | Person |
| Georges_Lautner | type | NamedIndividual |
| Georges_Lautner | label | "Georges Lautner" |
| La_Cage_aux_Folles_3_The_Wedding | type | Film |
| La_Cage_aux_Folles_3_The_Wedding | type | NamedIndividual |
| La_Cage_aux_Folles_3_The_Wedding | label | "La Cage Aux Folles 3: The Wedding" |
| Renée_Saint_Cyr | type | Person |
| Renée_Saint_Cyr | type | NamedIndividual |
| Renée_Saint_Cyr | label | "Renée Saint-Cyr" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
