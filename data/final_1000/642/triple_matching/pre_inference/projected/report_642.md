# Triple matching report: 642

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Lake_Powell | hasCountry | United_States |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Takhlakh_Lake | hasCountry | U_S |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Lake_Powell | type | Place |
| Lake_Powell | type | NamedIndividual |
| Lake_Powell | label | "Lake Powell" |
| Takhlakh_Lake | hasCountry | United_States |
| Takhlakh_Lake | type | Place |
| Takhlakh_Lake | type | NamedIndividual |
| Takhlakh_Lake | label | "Takhlakh Lake" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |
| United_States | altLabel | "U.S." |
| United_States | altLabel | "USA" |

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
