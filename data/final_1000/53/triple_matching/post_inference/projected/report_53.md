# Triple matching report: 53

# 1. Matched triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Housefull_2 | hasProducer | Sajid_Nadiadwala |
| Housefull_2 | type | Artifact |
| Housefull_2 | type | CreativeWork |
| Sajid_Nadiadwala | hasBirthDate | "1966-02-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sajid_Nadiadwala | type | Agent |
| Sajid_Nadiadwala | type | Person |
| Term_Life | hasProducer | Vince_Vaughn |
| Term_Life | type | Artifact |
| Term_Life | type | CreativeWork |
| Vince_Vaughn | hasBirthDate | "1970-03-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Vince_Vaughn | type | Agent |
| Vince_Vaughn | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Housefull_2 | type | Film |
| Term_Life | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 12 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.857143 |
| Recall | 1.000000 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
