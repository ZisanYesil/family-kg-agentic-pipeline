# Triple matching report: 666

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Hearts_in_Exile_1915_film | hasDirector | James_Young |
| Lawson_Harris | hasCountry | American |
| Sunshine_Sally | hasDirector | Lawson_Harris |

# 2. Unmatched triples

**Total unmatched count: 19**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| James_Young_director | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 18**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Hearts_in_Exile_1915_film | type | Film |
| Hearts_in_Exile_1915_film | type | NamedIndividual |
| Hearts_in_Exile_1915_film | label | "Hearts in Exile (1915 film)" |
| James_Young | hasCountry | American |
| James_Young | type | Person |
| James_Young | type | NamedIndividual |
| James_Young | label | "James Young" |
| Lawson_Harris | type | Person |
| Lawson_Harris | type | NamedIndividual |
| Lawson_Harris | label | "Lawson Harris" |
| Lawson_Harris | altLabel | "William Lawson Harris" |
| Sunshine_Sally | type | Film |
| Sunshine_Sally | type | NamedIndividual |
| Sunshine_Sally | label | "Sunshine Sally" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 21 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 22 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 18 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.142857 |
| Recall | 0.750000 |
| F1 score | 0.240000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
