# Triple matching report: 70

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Domenico_Cosselli | hasBirthDate | "1801-05-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Domenico_Cosselli | hasDeathDate | "1855-11-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Neil_Lloyd_Macky | hasBirthDate | "1891-02-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Neil_Lloyd_Macky | hasDeathDate | "1981-10-04"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Domenico_Cosselli | type | Person |
| Domenico_Cosselli | type | NamedIndividual |
| Domenico_Cosselli | label | "Domenico Cosselli" |
| Neil_Lloyd_Macky | type | Person |
| Neil_Lloyd_Macky | type | NamedIndividual |
| Neil_Lloyd_Macky | label | "Neil Lloyd Macky" |

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
