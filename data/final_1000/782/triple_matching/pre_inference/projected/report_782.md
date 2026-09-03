# Triple matching report: 782

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jan_Karol_Opaliński | hasParent | Krzysztof_Opaliński |
| Krzysztof_Opaliński | hasCountry | Polish_Lithuanian_Commonwealth |

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
| Jan_Karol_Opaliński | type | Person |
| Jan_Karol_Opaliński | type | NamedIndividual |
| Jan_Karol_Opaliński | label | "Jan Karol Opaliński" |
| Krzysztof_Opaliński | type | Person |
| Krzysztof_Opaliński | type | NamedIndividual |
| Krzysztof_Opaliński | label | "Krzysztof Opaliński" |
| Polish_Lithuanian_Commonwealth | type | Country |
| Polish_Lithuanian_Commonwealth | type | NamedIndividual |
| Polish_Lithuanian_Commonwealth | label | "Poland" |
| Polish_Lithuanian_Commonwealth | altLabel | "Polish" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
