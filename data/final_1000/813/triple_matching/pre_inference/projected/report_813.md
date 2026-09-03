# Triple matching report: 813

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gas | hasDirector | Henry_Chan |
| Henry_Chan | hasAwardReceived | Primetime_Emmy_Award |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Gas | type | Film |
| Gas | type | NamedIndividual |
| Gas | label | "Gas (2004 film)" |
| Henry_Chan | type | Person |
| Henry_Chan | type | NamedIndividual |
| Henry_Chan | label | "Henry Chan" |
| Primetime_Emmy_Award | type | Award |
| Primetime_Emmy_Award | type | NamedIndividual |
| Primetime_Emmy_Award | label | "Primetime Emmy Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
