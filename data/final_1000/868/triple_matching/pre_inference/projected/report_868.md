# Triple matching report: 868

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Stanisław_Koniecpolski | hasCountry | Polish_Lithuanian_Commonwealth |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Aleksander_Koniecpolski | hasParent | Stanisław_Koniecpolski |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Aleksander_Koniecpolski | type | Person |
| Aleksander_Koniecpolski | type | NamedIndividual |
| Aleksander_Koniecpolski | label | "Aleksander Koniecpolski (1620–1659)" |
| Polish_Lithuanian_Commonwealth | type | Country |
| Polish_Lithuanian_Commonwealth | type | NamedIndividual |
| Polish_Lithuanian_Commonwealth | label | "Poland" |
| Polish_Lithuanian_Commonwealth | altLabel | "Polish" |
| Stanisław_Koniecpolski | hasChild | Aleksander_Koniecpolski |
| Stanisław_Koniecpolski | type | Person |
| Stanisław_Koniecpolski | type | NamedIndividual |
| Stanisław_Koniecpolski | label | "Stanisław Koniecpolski" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
