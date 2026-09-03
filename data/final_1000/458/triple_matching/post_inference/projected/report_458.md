# Triple matching report: 458

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| A_Summer_You_Will_Never_Forget | hasCountry | German |
| A_Summer_You_Will_Never_Forget | type | Artifact |
| Alfred_von_Ingelheim_s_Dramatic_Life | hasCountry | German |
| Alfred_von_Ingelheim_s_Dramatic_Life | type | Artifact |
| German | type | Country |
| German | type | Place |

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
| A_Summer_You_Will_Never_Forget | type | CreativeWork |
| A_Summer_You_Will_Never_Forget | type | Film |
| Alfred_von_Ingelheim_s_Dramatic_Life | type | CreativeWork |
| Alfred_von_Ingelheim_s_Dramatic_Life | type | Film |

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
