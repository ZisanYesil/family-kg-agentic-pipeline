# Triple matching report: 592

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Vujadin_Boškov | hasBirthDate | "1931-05-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Vujadin_Boškov | hasDeathDate | "2014-04-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_P_Holaday | hasBirthDate | "1882-12-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_P_Holaday | hasDeathDate | "1946-01-29"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Vujadin_Boškov | type | Person |
| Vujadin_Boškov | type | NamedIndividual |
| Vujadin_Boškov | label | "Vujadin Boškov" |
| William_P_Holaday | type | Person |
| William_P_Holaday | type | NamedIndividual |
| William_P_Holaday | label | "William P. Holaday" |

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
