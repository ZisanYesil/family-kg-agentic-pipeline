# Triple matching report: 272

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Osborne_Computer_Corporation | hasFounder | Adam_Osborne |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Adam_Osborne | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Adam_Osborne | type | Person |
| Adam_Osborne | type | NamedIndividual |
| Adam_Osborne | label | "Adam Osborne" |
| Osborne_Computer_Corporation | type | Organization |
| Osborne_Computer_Corporation | type | NamedIndividual |
| Osborne_Computer_Corporation | label | "Osborne Computer Corporation" |
| thailand | type | Country |
| thailand | type | NamedIndividual |
| thailand | label | "Thailand" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
