# Triple matching report: 584

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Andrew_Lloyd_Webber | hasSpouse | Sarah_Brightman |
| Andrew_Lloyd_Webber | type | Agent |
| Andrew_Lloyd_Webber | type | Person |
| Angel | hasCreator | Sarah_Brightman |
| Angel | hasPerformer | Sarah_Brightman |
| Angel | type | Artifact |
| Angel | type | CreativeWork |
| Sarah_Brightman | hasSpouse | Andrew_Lloyd_Webber |
| Sarah_Brightman | type | Agent |
| Sarah_Brightman | type | Person |

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
| Angel | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 11 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.909091 |
| Recall | 1.000000 |
| F1 score | 0.952381 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
