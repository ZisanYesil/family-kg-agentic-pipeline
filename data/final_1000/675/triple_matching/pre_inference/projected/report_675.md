# Triple matching report: 675

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Trudeliese_Schmidt | hasBirthDate | "1942-11-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Trudeliese_Schmidt | hasDeathDate | "2004-06-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Yardena_Alotin | hasBirthDate | "1930-04-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Yardena_Alotin | hasDeathDate | "1994-10-04"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Trudeliese_Schmidt | type | Person |
| Trudeliese_Schmidt | type | NamedIndividual |
| Trudeliese_Schmidt | label | "Trudeliese Schmidt" |
| Trudeliese_Schmidt | altLabel | "Trudeliese Schmidt" |
| Yardena_Alotin | type | Person |
| Yardena_Alotin | type | NamedIndividual |
| Yardena_Alotin | label | "Yardena Alotin" |
| Yardena_Alotin | altLabel | "Yardena Alotin" |

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
