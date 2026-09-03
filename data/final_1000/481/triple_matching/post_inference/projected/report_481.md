# Triple matching report: 481

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Come_and_See | hasCountry | Soviet |
| Come_and_See | type | Artifact |
| Soviet | type | Country |
| Soviet | type | Place |
| The_Diplomatic_Pouch | hasCountry | Soviet |
| The_Diplomatic_Pouch | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Come_and_See | type | CreativeWork |
| Come_and_See | type | Film |
| The_Diplomatic_Pouch | type | CreativeWork |
| The_Diplomatic_Pouch | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.600000 |
| Recall | 1.000000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
