# Triple matching report: 156

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Other_Half_2016_film | hasCountry | Canadian |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Spy_Kids_2_The_Island_of_Lost_Dreams | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Canadian | type | Country |
| Canadian | type | NamedIndividual |
| Canadian | label | "Canada" |
| Spy_Kids_2_The_Island_of_Lost_Dreams | hasCountry | united_states_country |
| Spy_Kids_2_The_Island_of_Lost_Dreams | type | Film |
| Spy_Kids_2_The_Island_of_Lost_Dreams | type | NamedIndividual |
| Spy_Kids_2_The_Island_of_Lost_Dreams | label | "Spy Kids 2: The Island of Lost Dreams" |
| The_Other_Half_2016_film | type | Film |
| The_Other_Half_2016_film | type | NamedIndividual |
| The_Other_Half_2016_film | label | "The Other Half (2016 film)" |
| united_states_country | type | Country |
| united_states_country | type | NamedIndividual |
| united_states_country | label | "United States" |

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
