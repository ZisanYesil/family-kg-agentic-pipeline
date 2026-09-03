# Triple matching report: 427

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Enrique_Iglesias | hasCountry | Spanish |
| Enrique_Iglesias | type | Agent |
| Enrique_Iglesias | type | Person |
| Heart_Attack | hasCreator | Enrique_Iglesias |
| Heart_Attack | hasPerformer | Enrique_Iglesias |
| Heart_Attack | type | Artifact |
| Heart_Attack | type | CreativeWork |
| Spanish | type | Country |
| Spanish | type | Place |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Enrique_Iglesias | hasCountry | country_philippines |
| country_philippines | type | Country |
| country_philippines | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
