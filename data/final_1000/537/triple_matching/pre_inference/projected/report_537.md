# Triple matching report: 537

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Billy_Murray | hasCountry | United_States |
| Bon_Bon_Buddy | hasPerformer | Billy_Murray |

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
| Billy_Murray | type | Person |
| Billy_Murray | type | NamedIndividual |
| Billy_Murray | label | "Billy Murray" |
| Bon_Bon_Buddy | type | MusicalWork |
| Bon_Bon_Buddy | type | NamedIndividual |
| Bon_Bon_Buddy | label | "Bon Bon Buddy" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |
| United_States | altLabel | "American" |

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
