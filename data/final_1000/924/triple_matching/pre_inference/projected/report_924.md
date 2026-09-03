# Triple matching report: 924

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Khalil_El_Amin | hasCountry | American |
| Tori_Anthony | hasCountry | American |

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
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Khalil_El_Amin | type | Person |
| Khalil_El_Amin | type | NamedIndividual |
| Khalil_El_Amin | label | "Khalil Hassan El-Amin" |
| Khalil_El_Amin | altLabel | "Khalil El-Amin" |
| Tori_Anthony | type | Person |
| Tori_Anthony | type | NamedIndividual |
| Tori_Anthony | label | "Tori Anthony" |

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
