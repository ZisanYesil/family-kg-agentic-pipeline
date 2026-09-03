# Triple matching report: 256

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| O_P_Nayyar | hasAwardReceived | Filmfare_Award |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Howrah_Bridge | hasComposer | O_P_Nayyar |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Award | type | Award |
| Filmfare_Award | type | NamedIndividual |
| Filmfare_Award | label | "Filmfare Award for Best Music Director" |
| Howrah_Bridge | type | Film |
| Howrah_Bridge | type | NamedIndividual |
| Howrah_Bridge | label | "Howrah Bridge" |
| O_P_Nayyar | type | Person |
| O_P_Nayyar | type | NamedIndividual |
| O_P_Nayyar | label | "O. P. Nayyar" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
