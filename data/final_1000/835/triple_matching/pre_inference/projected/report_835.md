# Triple matching report: 835

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ruth_M_Kirk | hasBirthDate | "1930-02-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ruth_M_Kirk | hasDeathDate | "2011-06-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Theron_Strinden | hasBirthDate | "1919-05-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Theron_Strinden | hasDeathDate | "2011-03-03"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Ruth_M_Kirk | type | Person |
| Ruth_M_Kirk | type | NamedIndividual |
| Ruth_M_Kirk | label | "Ruth M. Kirk" |
| Theron_Strinden | type | Person |
| Theron_Strinden | type | NamedIndividual |
| Theron_Strinden | label | "Theron Strinden" |

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
