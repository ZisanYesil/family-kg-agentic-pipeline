# Triple matching report: 455

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Philip_Foster_Farm | hasCountry | United_States |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Seattle_Times_Building | hasCountry | Canadian |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Philip_Foster_Farm | type | Artifact |
| Philip_Foster_Farm | type | NamedIndividual |
| Philip_Foster_Farm | label | "Philip Foster Farm" |
| Philip_Foster_Farm | altLabel | "Philip Foster Farm" |
| Seattle_Times_Building | hasCountry | United_States |
| Seattle_Times_Building | type | Artifact |
| Seattle_Times_Building | type | NamedIndividual |
| Seattle_Times_Building | label | "Seattle Times Building" |
| Seattle_Times_Building | altLabel | "Seattle Times Building" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |
| United_States | altLabel | "United States" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
