# Triple matching report: 992

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| I_ll_Get_By_film | hasDirector | Richard_Sale |
| The_Reincarnation_of_Golden_Lotus | hasDirector | Clara_Law |

# 2. Unmatched triples

**Total unmatched count: 25**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Clara_Law | hasCountry | Australia |
| Richard_Sale_director | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 23**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Clara_Law | hasCountry | country_hong_kong |
| Clara_Law | type | Person |
| Clara_Law | type | NamedIndividual |
| Clara_Law | label | "Clara Law" |
| Clara_Law | altLabel | "Clara Law Cheuk-yiu" |
| I_ll_Get_By_film | type | Film |
| I_ll_Get_By_film | type | NamedIndividual |
| I_ll_Get_By_film | label | "I'll Get By" |
| Richard_Sale | hasCountry | American |
| Richard_Sale | type | Person |
| Richard_Sale | type | NamedIndividual |
| Richard_Sale | label | "Richard Sale" |
| The_Reincarnation_of_Golden_Lotus | type | Film |
| The_Reincarnation_of_Golden_Lotus | type | NamedIndividual |
| The_Reincarnation_of_Golden_Lotus | label | "The Reincarnation of Golden Lotus" |
| country_hong_kong | type | Country |
| country_hong_kong | type | NamedIndividual |
| country_hong_kong | label | "Hong Kong" |
| country_hong_kong | altLabel | "Hong Kong" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 25 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 27 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 23 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.080000 |
| Recall | 0.500000 |
| F1 score | 0.137931 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
