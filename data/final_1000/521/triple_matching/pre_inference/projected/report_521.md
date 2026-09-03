# Triple matching report: 521

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| ULTRA_Diamonds | hasCountry | United_States |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Dillon_Dam_Brewery | hasCountry | U_S_A |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Dillon_Dam_Brewery | hasCountry | United_States |
| Dillon_Dam_Brewery | type | Organization |
| Dillon_Dam_Brewery | type | NamedIndividual |
| Dillon_Dam_Brewery | label | "Dillon Dam Brewery" |
| ULTRA_Diamonds | type | Organization |
| ULTRA_Diamonds | type | NamedIndividual |
| ULTRA_Diamonds | label | "ULTRA Diamonds" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |
| United_States | altLabel | "U.S.A." |
| United_States | altLabel | "United States of America" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
