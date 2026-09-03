# Triple matching report: 53

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Housefull_2 | hasProducer | Sajid_Nadiadwala |
| Sajid_Nadiadwala | hasBirthDate | "1966-02-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Term_Life | hasProducer | Vince_Vaughn |
| Vince_Vaughn | hasBirthDate | "1970-03-28"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Housefull_2 | type | Film |
| Housefull_2 | type | NamedIndividual |
| Housefull_2 | label | "Housefull 2" |
| Sajid_Nadiadwala | type | Person |
| Sajid_Nadiadwala | type | NamedIndividual |
| Sajid_Nadiadwala | label | "Sajid Nadiadwala" |
| Term_Life | type | Film |
| Term_Life | type | NamedIndividual |
| Term_Life | label | "Term Life" |
| Vince_Vaughn | type | Person |
| Vince_Vaughn | type | NamedIndividual |
| Vince_Vaughn | label | "Vince Vaughn" |
| Vince_Vaughn | altLabel | "Vincent Anthony Vaughn" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 17 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.235294 |
| Recall | 1.000000 |
| F1 score | 0.380952 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
