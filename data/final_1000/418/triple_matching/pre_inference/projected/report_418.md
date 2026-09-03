# Triple matching report: 418

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Tsai_Cheng_fu | hasBirthDate | "1929"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Tsai_Cheng_fu | hasDeathDate | "2016-07-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_H_Maynard | hasBirthDate | "1786-11-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_H_Maynard | hasDeathDate | "1832-08-28"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Tsai_Cheng_fu | type | Person |
| Tsai_Cheng_fu | type | NamedIndividual |
| Tsai_Cheng_fu | label | "Tsai Cheng-Fu" |
| William_H_Maynard | type | Person |
| William_H_Maynard | type | NamedIndividual |
| William_H_Maynard | label | "William H. Maynard" |

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
