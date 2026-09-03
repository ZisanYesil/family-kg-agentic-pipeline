# Triple matching report: 553

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Jean_Grémillon | hasBirthDate | "1901-10-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_Grémillon | hasDeathDate | "1959-11-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ángel_Recasens | hasBirthDate | "1938-03-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ángel_Recasens | hasDeathDate | "2007-08-02"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Jean_Grémillon | type | Person |
| Jean_Grémillon | type | NamedIndividual |
| Jean_Grémillon | label | "Jean Grémillon" |
| Ángel_Recasens | type | Person |
| Ángel_Recasens | type | NamedIndividual |
| Ángel_Recasens | label | "Ángel Recasens" |

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
