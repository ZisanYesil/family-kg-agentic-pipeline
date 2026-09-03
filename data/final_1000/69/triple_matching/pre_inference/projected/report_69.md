# Triple matching report: 69

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Philippe_Solari | hasBirthDate | "1840-05-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Philippe_Solari | hasDeathDate | "1906-01-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Stephen_Jurika | hasBirthDate | "1910-12-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Stephen_Jurika | hasDeathDate | "1993-07-15"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Philippe_Solari | type | Person |
| Philippe_Solari | type | NamedIndividual |
| Philippe_Solari | label | "Philippe Solari" |
| Stephen_Jurika | type | Person |
| Stephen_Jurika | type | NamedIndividual |
| Stephen_Jurika | label | "Stephen Jurika Jr." |
| Stephen_Jurika | altLabel | "Stephen Jurika" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
