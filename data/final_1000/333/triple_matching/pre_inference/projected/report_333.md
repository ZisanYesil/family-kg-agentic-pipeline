# Triple matching report: 333

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ernst_Bessey | hasBirthDate | "1877-02-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ernst_Bessey | hasDeathDate | "1957-07-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Friedrich_Paschen | hasBirthDate | "1865-01-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Friedrich_Paschen | hasDeathDate | "1947-02-25"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Ernst_Bessey | type | Person |
| Ernst_Bessey | type | NamedIndividual |
| Ernst_Bessey | label | "Ernst Bessey" |
| Ernst_Bessey | altLabel | "Ernst Athearn Bessey" |
| Friedrich_Paschen | type | Person |
| Friedrich_Paschen | type | NamedIndividual |
| Friedrich_Paschen | label | "Friedrich Paschen" |
| Friedrich_Paschen | altLabel | "Louis Carl Heinrich Friedrich Paschen" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.333333 |
| Recall | 1.000000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
