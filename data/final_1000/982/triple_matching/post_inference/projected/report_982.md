# Triple matching report: 982

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Mason | type | Agent |
| Herbert_Mason | type | Person |
| Strange_Boarders | hasCreator | Herbert_Mason |
| Strange_Boarders | hasDirector | Herbert_Mason |
| Strange_Boarders | type | Artifact |
| Strange_Boarders | type | CreativeWork |
| Strange_Boarders | type | Film |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Birmingham | type | Place |
| Herbert_Mason | hasBirthPlace | Birmingham |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 9 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.777778 |
| F1 score | 0.875000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
