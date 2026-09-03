# Triple matching report: 990

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| David_Faurschou | hasBirthDate | "1956-01-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Osita_Chidoka | hasBirthDate | "1971-07-18"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| David_Faurschou | type | Person |
| David_Faurschou | type | NamedIndividual |
| David_Faurschou | label | "David Faurschou" |
| Osita_Chidoka | type | Person |
| Osita_Chidoka | type | NamedIndividual |
| Osita_Chidoka | label | "Osita Benjamin Chidoka" |
| Osita_Chidoka | altLabel | "Osita Chidoka" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
