# Triple matching report: 84

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Agents_of_Good_Roots | hasCountry | American |
| The_Human_League | hasCountry | British |

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
| British | altLabel | "English" |
| agents_of_good_roots | hasCountry | American |
| agents_of_good_roots | type | Organization |
| agents_of_good_roots | type | NamedIndividual |
| agents_of_good_roots | label | "Agents of Good Roots" |
| the_human_league | hasCountry | British |
| the_human_league | type | Organization |
| the_human_league | type | NamedIndividual |
| the_human_league | label | "The Human League" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 18 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
