# Triple matching report: 229

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| It_s_a_Great_Feeling | hasDirector | David_Butler |
| Oklahoma_1999_film | hasDirector | Trevor_Nunn |
| Trevor_Nunn | hasCountry | British |

# 2. Unmatched triples

**Total unmatched count: 22**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| David_Butler_director | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 21**

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
| David_Butler | hasCountry | American |
| David_Butler | type | Person |
| David_Butler | type | NamedIndividual |
| David_Butler | label | "David Butler" |
| It_s_a_Great_Feeling | type | Film |
| It_s_a_Great_Feeling | type | NamedIndividual |
| It_s_a_Great_Feeling | label | "It's a Great Feeling" |
| Oklahoma_1999_film | type | Film |
| Oklahoma_1999_film | type | NamedIndividual |
| Oklahoma_1999_film | label | "Oklahoma! (1999 film)" |
| Trevor_Nunn | type | Person |
| Trevor_Nunn | type | NamedIndividual |
| Trevor_Nunn | label | "Trevor Nunn" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 24 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 25 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 21 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.750000 |
| F1 score | 0.214286 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
