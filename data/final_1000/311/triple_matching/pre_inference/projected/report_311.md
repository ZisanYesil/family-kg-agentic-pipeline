# Triple matching report: 311

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| My_Father_the_Hero_1994_film | hasCountry | American |
| My_Father_the_Hero_1994_film | hasCountry | French |
| Wyoming_Roundup | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| My_Father_the_Hero_1994_film | type | Film |
| My_Father_the_Hero_1994_film | type | NamedIndividual |
| My_Father_the_Hero_1994_film | label | "My Father the Hero (1994 film)" |
| Wyoming_Roundup | type | Film |
| Wyoming_Roundup | type | NamedIndividual |
| Wyoming_Roundup | label | "Wyoming Roundup" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 17 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.176471 |
| Recall | 1.000000 |
| F1 score | 0.300000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
