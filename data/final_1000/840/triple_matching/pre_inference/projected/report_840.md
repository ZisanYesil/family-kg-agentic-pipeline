# Triple matching report: 840

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Manoranjan | hasDirector | Shammi_Kapoor |
| Shammi_Kapoor | hasAwardReceived | Filmfare_Award |

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
| Filmfare_Award | type | Award |
| Filmfare_Award | type | NamedIndividual |
| Filmfare_Award | label | "Filmfare Best Actor Award" |
| Manoranjan | type | Film |
| Manoranjan | type | NamedIndividual |
| Manoranjan | label | "Manoranjan" |
| Shammi_Kapoor | hasAwardReceived | filmfare_best_supporting_actor_award_1982 |
| Shammi_Kapoor | type | Person |
| Shammi_Kapoor | type | NamedIndividual |
| Shammi_Kapoor | label | "Shammi Kapoor" |
| filmfare_best_supporting_actor_award_1982 | type | Award |
| filmfare_best_supporting_actor_award_1982 | type | NamedIndividual |
| filmfare_best_supporting_actor_award_1982 | label | "Filmfare Award for Best Supporting Actor" |

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
