# Triple matching report: 203

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Lover_s_Prayer | hasCountry | American |
| Lover_s_Prayer | hasCountry | British |
| Make_Up_1937_film | hasCountry | British |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "British" |
| Lover_s_Prayer | type | Film |
| Lover_s_Prayer | type | NamedIndividual |
| Lover_s_Prayer | label | "Lover's Prayer" |
| Lover_s_Prayer | altLabel | "Lover's Prayer" |
| Make_Up_1937_film | type | Film |
| Make_Up_1937_film | type | NamedIndividual |
| Make_Up_1937_film | label | "Make-Up (1937 film)" |
| Make_Up_1937_film | altLabel | "Make-Up (1937 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 19 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.157895 |
| Recall | 1.000000 |
| F1 score | 0.272727 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
