# Triple matching report: 716

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| George_F_Sowers | hasBirthDate | "1921-09-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_F_Sowers | hasDeathDate | "1996-10-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henrietta_Amelia_Leeson | hasBirthDate | "1751"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Henrietta_Amelia_Leeson | hasDeathDate | "1826"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| George_F_Sowers | type | Person |
| George_F_Sowers | type | NamedIndividual |
| George_F_Sowers | label | "George F. Sowers" |
| Henrietta_Amelia_Leeson | type | Person |
| Henrietta_Amelia_Leeson | type | NamedIndividual |
| Henrietta_Amelia_Leeson | label | "Henrietta Amelia Leeson" |

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
