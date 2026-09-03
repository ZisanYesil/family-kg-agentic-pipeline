# Triple matching report: 958

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Annanias_Mathe | hasDeathDate | "2016-12-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sigfrid_Jacobsson | hasDeathDate | "1961-07-20"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Annanias_Mathe | type | Person |
| Annanias_Mathe | type | NamedIndividual |
| Annanias_Mathe | label | "Annanias Mathe" |
| Annanias_Mathe | altLabel | "Ananias Mathe" |
| Sigfrid_Jacobsson | type | Person |
| Sigfrid_Jacobsson | type | NamedIndividual |
| Sigfrid_Jacobsson | label | "Sigfrid Jacobsson" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
