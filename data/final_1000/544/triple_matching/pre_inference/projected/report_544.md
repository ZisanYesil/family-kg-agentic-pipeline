# Triple matching report: 544

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gottfried_Baist | hasBirthDate | "1853-02-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gottfried_Baist | hasDeathDate | "1920-10-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Mignon_McLaughlin | hasBirthDate | "1913-06-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Mignon_McLaughlin | hasDeathDate | "1983-12-20"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Gottfried_Baist | type | Person |
| Gottfried_Baist | type | NamedIndividual |
| Gottfried_Baist | label | "Gottfried Baist" |
| Mignon_McLaughlin | type | Person |
| Mignon_McLaughlin | type | NamedIndividual |
| Mignon_McLaughlin | label | "Mignon McLaughlin" |

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
