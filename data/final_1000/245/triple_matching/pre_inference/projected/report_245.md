# Triple matching report: 245

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Miklós_László | hasBirthDate | "1903-05-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Miklós_László | hasDeathDate | "1973-04-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Xu_Yulan | hasBirthDate | "1921-12-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Xu_Yulan | hasDeathDate | "2017-04-19"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Miklós_László | type | Person |
| Miklós_László | type | NamedIndividual |
| Miklós_László | label | "Miklos László" |
| Miklós_László | altLabel | "Miklos Laszlo" |
| Xu_Yulan | type | Person |
| Xu_Yulan | type | NamedIndividual |
| Xu_Yulan | label | "Xu Yulan" |
| Xu_Yulan | altLabel | "Xu Yulan" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.333333 |
| Recall | 1.000000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
