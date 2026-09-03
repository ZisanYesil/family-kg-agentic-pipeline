# Triple matching report: 424

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Alice_K_Bache | hasBirthDate | "1903"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Alice_K_Bache | hasDeathDate | "1977"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Ma_Xisheng | hasBirthDate | "0899"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Ma_Xisheng | hasDeathDate | "0932-08-15"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Alice_K_Bache | type | Person |
| Alice_K_Bache | type | NamedIndividual |
| Alice_K_Bache | label | "Alice K. Bache" |
| Ma_Xisheng | type | Person |
| Ma_Xisheng | type | NamedIndividual |
| Ma_Xisheng | label | "Ma Xisheng" |

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
