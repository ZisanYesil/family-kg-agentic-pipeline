# Triple matching report: 183

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gunasekhar | hasAwardReceived | Filmfare_Awards_South |
| Nippu | hasDirector | Gunasekhar |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Awards_South | type | Award |
| Filmfare_Awards_South | type | NamedIndividual |
| Filmfare_Awards_South | label | "Filmfare Award for Best Director – Telugu" |
| Filmfare_Awards_South | altLabel | "Filmfare Award for Best Director – Telugu" |
| Gunasekhar | type | Person |
| Gunasekhar | type | NamedIndividual |
| Gunasekhar | label | "Gunasekhar" |
| Gunasekhar | altLabel | "Gunasekar" |
| Gunasekhar | altLabel | "Gunasekhar" |
| Nippu | type | Film |
| Nippu | type | NamedIndividual |
| Nippu | label | "Nippu" |
| Nippu | altLabel | "Nippu" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
