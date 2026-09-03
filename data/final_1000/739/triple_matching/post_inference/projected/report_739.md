# Triple matching report: 739

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Award_for_Best_Director | type | Award |
| Jo_Jeeta_Wohi_Sikandar | hasCreator | Mansoor_Khan |
| Jo_Jeeta_Wohi_Sikandar | hasDirector | Mansoor_Khan |
| Jo_Jeeta_Wohi_Sikandar | type | Artifact |
| Jo_Jeeta_Wohi_Sikandar | type | CreativeWork |
| Jo_Jeeta_Wohi_Sikandar | type | Film |
| Mansoor_Khan | hasAwardReceived | Filmfare_Award_for_Best_Director |
| Mansoor_Khan | type | Agent |
| Mansoor_Khan | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mansoor_Khan | hasAwardReceived | award_national_film_award_best_popular_film_providing_wholesome_entertainment |
| award_national_film_award_best_popular_film_providing_wholesome_entertainment | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.818182 |
| Recall | 1.000000 |
| F1 score | 0.900000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
