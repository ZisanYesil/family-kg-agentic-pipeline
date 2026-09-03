# Triple matching report: 253

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Curumsey_Damjee | hasBirthDate | "1844"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Curumsey_Damjee | hasDeathDate | "1918"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Octavius_Hammond | hasBirthDate | "1835-03-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Octavius_Hammond | hasDeathDate | "1908-08-22"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Curumsey_Damjee | type | Person |
| Curumsey_Damjee | type | NamedIndividual |
| Curumsey_Damjee | label | "Curumsey Damjee" |
| Curumsey_Damjee | altLabel | "Curumsey Damjee" |
| Curumsey_Damjee | altLabel | "Karamsi Damji" |
| Curumsey_Damjee | altLabel | "Kasamshi Damji" |
| Octavius_Hammond | type | Person |
| Octavius_Hammond | type | NamedIndividual |
| Octavius_Hammond | label | "Octavius Hammond" |
| Octavius_Hammond | altLabel | "Octavius Hammond" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 14 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.285714 |
| Recall | 1.000000 |
| F1 score | 0.444444 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
