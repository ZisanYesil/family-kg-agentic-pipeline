# Triple matching report: 156

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Canadian | type | Country |
| Canadian | type | Place |
| Spy_Kids_2_The_Island_of_Lost_Dreams | type | Artifact |
| The_Other_Half_2016_film | hasCountry | Canadian |
| The_Other_Half_2016_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Spy_Kids_2_The_Island_of_Lost_Dreams | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Spy_Kids_2_The_Island_of_Lost_Dreams | hasCountry | united_states_country |
| Spy_Kids_2_The_Island_of_Lost_Dreams | type | CreativeWork |
| Spy_Kids_2_The_Island_of_Lost_Dreams | type | Film |
| The_Other_Half_2016_film | type | CreativeWork |
| The_Other_Half_2016_film | type | Film |
| united_states_country | type | Country |
| united_states_country | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 15 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.416667 |
| Recall | 0.625000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
