# Triple matching report: 564

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Abdülaziz | hasSpouse | Hayranidil_Kadın |
| Abdülaziz | type | Agent |
| Abdülaziz | type | Person |
| Hayranidil_Kadın | hasSpouse | Abdülaziz |
| Hayranidil_Kadın | type | Agent |
| Hayranidil_Kadın | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Abdülaziz | hasDeathPlace | Constantinople |
| Constantinople | type | Place |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Abdülaziz | hasBirthDate | "1830-02-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Abdülaziz | hasDeathDate | "1876-06-04"^^<http://www.w3.org/2001/XMLSchema#date> |

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
