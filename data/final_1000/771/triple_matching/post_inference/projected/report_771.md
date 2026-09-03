# Triple matching report: 771

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Billy_Elliot | hasComposer | Stephen_Warbeck |
| Billy_Elliot | hasCreator | Stephen_Warbeck |
| Billy_Elliot | type | Artifact |
| Billy_Elliot | type | CreativeWork |
| Southampton_Hampshire | type | Place |
| Stephen_Warbeck | hasBirthPlace | Southampton_Hampshire |
| Stephen_Warbeck | type | Agent |
| Stephen_Warbeck | type | Person |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Billy_Elliot | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 9 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.888889 |
| Recall | 1.000000 |
| F1 score | 0.941176 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
