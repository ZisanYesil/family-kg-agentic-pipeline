# Triple matching report: 613

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Chou_Meng_tieh | hasBirthDate | "1921-12-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Chou_Meng_tieh | hasDeathDate | "2014-05-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Fredy_Schmidtke | hasBirthDate | "1961-07-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Fredy_Schmidtke | hasDeathDate | "2017-12-01"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Chou_Meng_tieh | type | Person |
| Chou_Meng_tieh | type | NamedIndividual |
| Chou_Meng_tieh | label | "Chou Meng-Tieh" |
| Fredy_Schmidtke | type | Person |
| Fredy_Schmidtke | type | NamedIndividual |
| Fredy_Schmidtke | label | "Fredy Schmidtke" |

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
