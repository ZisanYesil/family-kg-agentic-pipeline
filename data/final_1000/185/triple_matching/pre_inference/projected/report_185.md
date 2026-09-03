# Triple matching report: 185

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Jiří_Baumruk | hasBirthDate | "1930-06-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jiří_Baumruk | hasDeathDate | "1989-11-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Mathias_Rosenblad | hasBirthDate | "1758-06-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Mathias_Rosenblad | hasDeathDate | "1847-09-04"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Jiří_Baumruk | type | Person |
| Jiří_Baumruk | type | NamedIndividual |
| Jiří_Baumruk | label | "Jiří Baumruk" |
| Mathias_Rosenblad | type | Person |
| Mathias_Rosenblad | type | NamedIndividual |
| Mathias_Rosenblad | label | "Mathias Rosenblad" |

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
