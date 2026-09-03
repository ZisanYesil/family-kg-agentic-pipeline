# Triple matching report: 706

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| A_Place_of_Rage | hasDirector | Pratibha_Parmar |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pratibha_Parmar | hasAwardReceived | 100_Women |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| A_Place_of_Rage | type | Film |
| A_Place_of_Rage | type | NamedIndividual |
| A_Place_of_Rage | label | "A Place of Rage" |
| Pratibha_Parmar | hasAwardReceived | lifetime_achievement_award_san_francisco_frameline |
| Pratibha_Parmar | hasAwardReceived | visionary_award_one_in_ten_film_festival |
| Pratibha_Parmar | type | Person |
| Pratibha_Parmar | type | NamedIndividual |
| Pratibha_Parmar | label | "Pratibha Parmar" |
| lifetime_achievement_award_san_francisco_frameline | type | Award |
| lifetime_achievement_award_san_francisco_frameline | type | NamedIndividual |
| lifetime_achievement_award_san_francisco_frameline | label | "San Francisco Frameline Film Festival Lifetime Achievement Award" |
| visionary_award_one_in_ten_film_festival | type | Award |
| visionary_award_one_in_ten_film_festival | type | NamedIndividual |
| visionary_award_one_in_ten_film_festival | label | "Visionary Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.066667 |
| Recall | 0.500000 |
| F1 score | 0.117647 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
