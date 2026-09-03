# Triple matching report: 840

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Award | type | Award |
| Manoranjan | hasCreator | Shammi_Kapoor |
| Manoranjan | hasDirector | Shammi_Kapoor |
| Manoranjan | type | Artifact |
| Manoranjan | type | CreativeWork |
| Manoranjan | type | Film |
| Shammi_Kapoor | hasAwardReceived | Filmfare_Award |
| Shammi_Kapoor | type | Agent |
| Shammi_Kapoor | type | Person |

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
| Shammi_Kapoor | hasAwardReceived | filmfare_best_supporting_actor_award_1982 |
| filmfare_best_supporting_actor_award_1982 | type | Award |

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
