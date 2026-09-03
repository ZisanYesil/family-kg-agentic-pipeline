# Triple matching report: 739

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jo_Jeeta_Wohi_Sikandar | hasDirector | Mansoor_Khan |
| Mansoor_Khan | hasAwardReceived | Filmfare_Award_for_Best_Director |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Award_for_Best_Director | type | Award |
| Filmfare_Award_for_Best_Director | type | NamedIndividual |
| Filmfare_Award_for_Best_Director | label | "Filmfare Award for Best Director" |
| Jo_Jeeta_Wohi_Sikandar | type | Film |
| Jo_Jeeta_Wohi_Sikandar | type | NamedIndividual |
| Jo_Jeeta_Wohi_Sikandar | label | "Jo Jeeta Wohi Sikandar" |
| Mansoor_Khan | hasAwardReceived | award_national_film_award_best_popular_film_providing_wholesome_entertainment |
| Mansoor_Khan | type | Person |
| Mansoor_Khan | type | NamedIndividual |
| Mansoor_Khan | label | "Mansoor Khan" |
| award_national_film_award_best_popular_film_providing_wholesome_entertainment | type | Award |
| award_national_film_award_best_popular_film_providing_wholesome_entertainment | type | NamedIndividual |
| award_national_film_award_best_popular_film_providing_wholesome_entertainment | label | "National Film Award for Best Popular Film Providing Wholesome Entertainment" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
