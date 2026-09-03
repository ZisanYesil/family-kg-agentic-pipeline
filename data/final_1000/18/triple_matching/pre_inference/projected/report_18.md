# Triple matching report: 18

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Csaba_Pálinkás | hasBirthDate | "1959-06-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Csaba_Pálinkás | hasDeathDate | "2004-10-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henry_Scheffé | hasBirthDate | "1907-04-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henry_Scheffé | hasDeathDate | "1977-07-05"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Csaba_Pálinkás | type | Person |
| Csaba_Pálinkás | type | NamedIndividual |
| Csaba_Pálinkás | label | "Csaba Pálinkás" |
| Henry_Scheffé | type | Person |
| Henry_Scheffé | type | NamedIndividual |
| Henry_Scheffé | label | "Henry Scheffé" |

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
