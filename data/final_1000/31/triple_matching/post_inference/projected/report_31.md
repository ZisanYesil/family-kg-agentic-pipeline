# Triple matching report: 31

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Leona_Lewis | hasBirthPlace | London |
| Leona_Lewis | type | Agent |
| Leona_Lewis | type | Person |
| London | type | Place |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| I_See_You | hasCreator | Leona_Lewis |
| I_See_You | hasPerformer | Leona_Lewis |
| I_See_You | type | Artifact |
| I_See_You | type | CreativeWork |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 4 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 8 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 4 |
| Precision | 1.000000 |
| Recall | 0.500000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
