# Triple matching report: 564

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Hayranidil_Kadın | hasSpouse | Abdülaziz |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Abdülaziz | hasDeathPlace | Constantinople |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Abdülaziz | hasBirthDate | "1830-02-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Abdülaziz | hasDeathDate | "1876-06-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Abdülaziz | type | Person |
| Abdülaziz | type | NamedIndividual |
| Abdülaziz | label | "Abdülaziz" |
| Hayranidil_Kadın | type | Person |
| Hayranidil_Kadın | type | NamedIndividual |
| Hayranidil_Kadın | label | "Hayranidil Kadın" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.111111 |
| Recall | 0.500000 |
| F1 score | 0.181818 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
