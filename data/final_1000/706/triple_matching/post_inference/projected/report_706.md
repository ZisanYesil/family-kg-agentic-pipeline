# Triple matching report: 706

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| A_Place_of_Rage | hasCreator | Pratibha_Parmar |
| A_Place_of_Rage | hasDirector | Pratibha_Parmar |
| A_Place_of_Rage | type | Artifact |
| A_Place_of_Rage | type | CreativeWork |
| A_Place_of_Rage | type | Film |
| Pratibha_Parmar | type | Agent |
| Pratibha_Parmar | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| 100_Women | type | Award |
| Pratibha_Parmar | hasAwardReceived | 100_Women |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Pratibha_Parmar | hasAwardReceived | lifetime_achievement_award_san_francisco_frameline |
| Pratibha_Parmar | hasAwardReceived | visionary_award_one_in_ten_film_festival |
| lifetime_achievement_award_san_francisco_frameline | type | Award |
| visionary_award_one_in_ten_film_festival | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.636364 |
| Recall | 0.777778 |
| F1 score | 0.700000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
