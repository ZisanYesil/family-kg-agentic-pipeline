# Triple matching report: 492

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Jean_Marc_Barr | hasCountry | American |
| Jean_Marc_Barr | hasCountry | French |
| Lovers_1999_film | hasDirector | Jean_Marc_Barr |
| Pitch_Perfect_3 | hasDirector | Trish_Sie |
| Trish_Sie | hasCountry | American |

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
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Jean_Marc_Barr | type | Person |
| Jean_Marc_Barr | type | NamedIndividual |
| Jean_Marc_Barr | label | "Jean-Marc Barr" |
| Lovers_1999_film | type | Film |
| Lovers_1999_film | type | NamedIndividual |
| Lovers_1999_film | label | "Lovers (1999 film)" |
| Pitch_Perfect_3 | type | Film |
| Pitch_Perfect_3 | type | NamedIndividual |
| Pitch_Perfect_3 | label | "Pitch Perfect 3" |
| Trish_Sie | type | Person |
| Trish_Sie | type | NamedIndividual |
| Trish_Sie | label | "Trish Sie" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 25 |
| Ground-truth triples in scope | 5 |
| Union triples in scope | 25 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 20 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
