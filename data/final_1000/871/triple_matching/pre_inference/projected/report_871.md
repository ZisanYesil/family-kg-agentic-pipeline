# Triple matching report: 871

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ernest_William_Goodpasture | hasBirthDate | "1886-10-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ramón_Corona | hasBirthDate | "1837-10-18"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Ernest_William_Goodpasture | type | Person |
| Ernest_William_Goodpasture | type | NamedIndividual |
| Ernest_William_Goodpasture | label | "Ernest William Goodpasture" |
| Ramón_Corona | type | Person |
| Ramón_Corona | type | NamedIndividual |
| Ramón_Corona | label | "Ramón Corona" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
