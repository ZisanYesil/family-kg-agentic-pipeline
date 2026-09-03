# Triple matching report: 427

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Enrique_Iglesias | hasCountry | Spanish |
| Heart_Attack | hasPerformer | Enrique_Iglesias |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Enrique_Iglesias | hasCountry | country_philippines |
| Enrique_Iglesias | type | Person |
| Enrique_Iglesias | type | NamedIndividual |
| Enrique_Iglesias | label | "Enrique Iglesias" |
| Heart_Attack | type | CreativeWork |
| Heart_Attack | type | NamedIndividual |
| Heart_Attack | label | "Heart Attack (Enrique Iglesias song)" |
| Spanish | type | Country |
| Spanish | type | NamedIndividual |
| Spanish | label | "Spain" |
| Spanish | altLabel | "Spanish" |
| country_philippines | type | Country |
| country_philippines | type | NamedIndividual |
| country_philippines | label | "Philippines" |
| country_philippines | altLabel | "Filipino" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.117647 |
| Recall | 1.000000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
