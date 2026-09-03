# Triple matching report: 748

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Michael_Davitt | type | Agent |
| Michael_Davitt | type | Person |
| Varoujan_Hakhbandian | hasBirthDate | "1936-12-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Varoujan_Hakhbandian | hasDeathDate | "1977-09-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Varoujan_Hakhbandian | type | Agent |
| Varoujan_Hakhbandian | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Michael_Davitt | hasBirthDate | "1846-03-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Michael_Davitt | hasDeathDate | "1906-05-30"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Michael_Davitt | hasBirthDate | "1950-04-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Michael_Davitt | hasDeathDate | "2005-06-19"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.750000 |
| Recall | 0.750000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
