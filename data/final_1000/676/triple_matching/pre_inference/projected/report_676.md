# Triple matching report: 676

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Barry_Levinson | hasCountry | American |
| Rock_the_Kasbah_film | hasDirector | Barry_Levinson |
| Sidney_Olcott | hasCountry | Canadian |
| The_Irish_in_America | hasDirector | Sidney_Olcott |

# 2. Unmatched triples

**Total unmatched count: 20**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 20**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Barry_Levinson | type | Person |
| Barry_Levinson | type | NamedIndividual |
| Barry_Levinson | label | "Barry Levinson" |
| Canadian | type | Country |
| Canadian | type | NamedIndividual |
| Canadian | label | "Canada" |
| Canadian | altLabel | "Canadian" |
| Rock_the_Kasbah_film | type | Film |
| Rock_the_Kasbah_film | type | NamedIndividual |
| Rock_the_Kasbah_film | label | "Rock the Kasbah" |
| Sidney_Olcott | type | Person |
| Sidney_Olcott | type | NamedIndividual |
| Sidney_Olcott | label | "Sidney Olcott" |
| The_Irish_in_America | type | Film |
| The_Irish_in_America | type | NamedIndividual |
| The_Irish_in_America | label | "The Irish in America" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 24 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 24 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 20 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
