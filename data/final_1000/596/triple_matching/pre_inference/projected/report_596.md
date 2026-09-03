# Triple matching report: 596

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Miljenko_Hrkać | hasBirthDate | "1947-10-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Miljenko_Hrkać | hasDeathDate | "1978-01-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Chopin | hasBirthDate | "1827"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| William_Chopin | hasDeathDate | "1900-10-30"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Miljenko_Hrkać | type | Person |
| Miljenko_Hrkać | type | NamedIndividual |
| Miljenko_Hrkać | label | "Miljenko Hrkać" |
| William_Chopin | type | Person |
| William_Chopin | type | NamedIndividual |
| William_Chopin | label | "William Chopin" |

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
