# Triple matching report: 575

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gunnar_Wiklund | hasBirthDate | "1935-08-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gunnar_Wiklund | hasDeathDate | "1989-09-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_Rodolphe_Perronet | hasBirthDate | "1708-10-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_Rodolphe_Perronet | hasDeathDate | "1794-02-27"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Gunnar_Wiklund | type | Person |
| Gunnar_Wiklund | type | NamedIndividual |
| Gunnar_Wiklund | label | "Gunnar Wiklund" |
| Jean_Rodolphe_Perronet | type | Person |
| Jean_Rodolphe_Perronet | type | NamedIndividual |
| Jean_Rodolphe_Perronet | label | "Jean-Rodolphe Perronet" |

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
