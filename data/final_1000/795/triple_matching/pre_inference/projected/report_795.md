# Triple matching report: 795

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gabrielle_Robinne | hasCountry | French |
| Nicolas_François_Vuillaume | hasCountry | French |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Gabrielle_Robinne | type | Person |
| Gabrielle_Robinne | type | NamedIndividual |
| Gabrielle_Robinne | label | "Gabrielle Robinne" |
| Gabrielle_Robinne | altLabel | "Gabrielle Anna Charlotte Robinne" |
| Nicolas_François_Vuillaume | type | Person |
| Nicolas_François_Vuillaume | type | NamedIndividual |
| Nicolas_François_Vuillaume | label | "Nicolas François Vuillaume" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
