# Triple matching report: 480

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Erik_Ole_Bye | hasBirthDate | "1883-03-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Erik_Ole_Bye | hasDeathDate | "1953-05-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henry_Paget_2nd_Marquess_of_Anglesey | hasBirthDate | "1797-07-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henry_Paget_2nd_Marquess_of_Anglesey | hasDeathDate | "1869-02-07"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Erik_Ole_Bye | type | Person |
| Erik_Ole_Bye | type | NamedIndividual |
| Erik_Ole_Bye | label | "Erik Ole Bye" |
| Henry_Paget_2nd_Marquess_of_Anglesey | type | Person |
| Henry_Paget_2nd_Marquess_of_Anglesey | type | NamedIndividual |
| Henry_Paget_2nd_Marquess_of_Anglesey | label | "Henry Paget, 2nd Marquess of Anglesey" |

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
