# Triple matching report: 339

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ben_Cura | hasCountry | Argentine |
| Creditors | hasDirector | Ben_Cura |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Argentine | type | Country |
| Argentine | type | NamedIndividual |
| Argentine | label | "Argentina" |
| Argentine | altLabel | "Argentine" |
| Ben_Cura | hasCountry | united_kingdom |
| Ben_Cura | type | Person |
| Ben_Cura | type | NamedIndividual |
| Ben_Cura | label | "Ben Cura" |
| Creditors | type | Film |
| Creditors | type | NamedIndividual |
| Creditors | label | "Creditors (2015 film)" |
| united_kingdom | type | Country |
| united_kingdom | type | NamedIndividual |
| united_kingdom | label | "United Kingdom" |
| united_kingdom | altLabel | "British" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.117647 |
| Recall | 1.000000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
