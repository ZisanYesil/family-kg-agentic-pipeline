# Triple matching report: 959

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Basil_Dearden | hasDeathDate | "1971-03-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Cage_of_Gold | hasDirector | Basil_Dearden |
| Face_of_a_Fugitive | hasDirector | Paul_Wendkos |
| Paul_Wendkos | hasDeathDate | "2009-11-12"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Basil_Dearden | type | Person |
| Basil_Dearden | type | NamedIndividual |
| Basil_Dearden | label | "Basil Dearden" |
| Cage_of_Gold | type | Film |
| Cage_of_Gold | type | NamedIndividual |
| Cage_of_Gold | label | "Cage of Gold" |
| Face_of_a_Fugitive | type | Film |
| Face_of_a_Fugitive | type | NamedIndividual |
| Face_of_a_Fugitive | label | "Face of a Fugitive" |
| Paul_Wendkos | type | Person |
| Paul_Wendkos | type | NamedIndividual |
| Paul_Wendkos | label | "Paul Wendkos" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
