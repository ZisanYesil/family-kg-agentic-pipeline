# Triple matching report: 12

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Pleshkovo | hasCountry | Russia |
| Tomskoye_Amur_Oblast | hasCountry | Russia |

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
| Pleshkovo | type | Place |
| Pleshkovo | type | NamedIndividual |
| Pleshkovo | label | "Pleshkovo" |
| Russia | type | Country |
| Russia | type | NamedIndividual |
| Russia | label | "Russia" |
| Tomskoye_Amur_Oblast | type | Place |
| Tomskoye_Amur_Oblast | type | NamedIndividual |
| Tomskoye_Amur_Oblast | label | "Tomskoye" |

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
