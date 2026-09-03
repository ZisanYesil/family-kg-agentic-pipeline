# Triple matching report: 538

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Wise | hasChild | Susannah_Wise |
| Herbert_Wise | type | Agent |
| Herbert_Wise | type | Person |
| Reunion_at_Fairborough | hasCreator | Herbert_Wise |
| Reunion_at_Fairborough | hasDirector | Herbert_Wise |
| Reunion_at_Fairborough | type | Artifact |
| Reunion_at_Fairborough | type | CreativeWork |
| Reunion_at_Fairborough | type | Film |
| Susannah_Wise | hasParent | Herbert_Wise |
| Susannah_Wise | type | Agent |
| Susannah_Wise | type | Person |

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
| Herbert_Wise | hasChild | charlie_walker_wise |
| charlie_walker_wise | hasParent | Herbert_Wise |
| charlie_walker_wise | type | Agent |
| charlie_walker_wise | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.733333 |
| Recall | 1.000000 |
| F1 score | 0.846154 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
