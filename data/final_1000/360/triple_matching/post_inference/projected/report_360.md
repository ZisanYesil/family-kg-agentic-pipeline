# Triple matching report: 360

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Brown | hasAwardReceived | Grammy_Award_for_Best_R_B_Album |
| Chris_Brown | type | Agent |
| Grammy_Award_for_Best_R_B_Album | type | Award |
| Little_More_Royalty | hasCreator | Chris_Brown |
| Little_More_Royalty | hasPerformer | Chris_Brown |
| Little_More_Royalty | type | Artifact |
| Little_More_Royalty | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Brown | hasAwardReceived | award_bet |
| Chris_Brown | hasAwardReceived | award_billboard_music |
| Chris_Brown | hasAwardReceived | award_soul_train_music |
| Chris_Brown | type | Person |
| award_bet | type | Award |
| award_billboard_music | type | Award |
| award_soul_train_music | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 14 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.500000 |
| Recall | 1.000000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
