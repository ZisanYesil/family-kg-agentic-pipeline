# Triple matching report: 484

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Agnès_Varda | hasCountry | French |
| Black_Panthers | hasDirector | Agnès_Varda |

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
| Agnès_Varda | type | Person |
| Agnès_Varda | type | NamedIndividual |
| Agnès_Varda | label | "Agnès Varda" |
| Black_Panthers | type | Film |
| Black_Panthers | type | NamedIndividual |
| Black_Panthers | label | "Black Panthers" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |

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
