# Triple matching report: 301

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ingrith_Johnson_Deyrup_Olsen | hasBirthDate | "1919"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Ingrith_Johnson_Deyrup_Olsen | hasDeathDate | "2004-07-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pierre_Sonnerat | hasBirthDate | "1748-08-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pierre_Sonnerat | hasDeathDate | "1814-03-31"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Ingrith_Johnson_Deyrup_Olsen | type | Person |
| Ingrith_Johnson_Deyrup_Olsen | type | NamedIndividual |
| Ingrith_Johnson_Deyrup_Olsen | label | "Ingrith Johnson Deyrup-Olsen" |
| Pierre_Sonnerat | type | Person |
| Pierre_Sonnerat | type | NamedIndividual |
| Pierre_Sonnerat | label | "Pierre Sonnerat" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
