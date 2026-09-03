# Triple matching report: 285

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Starter_for_10_film | hasCountry | British |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Starter_for_10_film | hasCountry | US |
| The_Urethra_Chronicles | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "British" |
| Starter_for_10_film | type | Film |
| Starter_for_10_film | type | NamedIndividual |
| Starter_for_10_film | label | "Starter for 10" |
| The_Urethra_Chronicles | type | Film |
| The_Urethra_Chronicles | type | NamedIndividual |
| The_Urethra_Chronicles | label | "The Urethra Chronicles" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.090909 |
| Recall | 0.333333 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
