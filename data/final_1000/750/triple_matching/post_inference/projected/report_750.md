# Triple matching report: 750

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Georges_Lautner | hasParent | Renée_Saint_Cyr |
| Georges_Lautner | type | Agent |
| Georges_Lautner | type | Person |
| La_Cage_aux_Folles_3_The_Wedding | hasCreator | Georges_Lautner |
| La_Cage_aux_Folles_3_The_Wedding | hasDirector | Georges_Lautner |
| La_Cage_aux_Folles_3_The_Wedding | type | Artifact |
| La_Cage_aux_Folles_3_The_Wedding | type | CreativeWork |
| La_Cage_aux_Folles_3_The_Wedding | type | Film |
| Renée_Saint_Cyr | hasChild | Georges_Lautner |
| Renée_Saint_Cyr | type | Agent |
| Renée_Saint_Cyr | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Georges_Lautner | hasBirthDate | "1926-01-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Georges_Lautner | hasDeathDate | "2013-11-22"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 13 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.846154 |
| Recall | 1.000000 |
| F1 score | 0.916667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
