# Triple matching report: 65

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Future_Medicine | hasCountry | United_Kingdom |
| Personalized_Medicine | hasPublisher | Future_Medicine |

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
| Future_Medicine | type | Organization |
| Future_Medicine | type | NamedIndividual |
| Future_Medicine | label | "Future Medicine" |
| Personalized_Medicine | type | CreativeWork |
| Personalized_Medicine | type | NamedIndividual |
| Personalized_Medicine | label | "Personalized Medicine" |
| United_Kingdom | type | Country |
| United_Kingdom | type | NamedIndividual |
| United_Kingdom | label | "United Kingdom" |
| United_Kingdom | altLabel | "United Kingdom" |

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
