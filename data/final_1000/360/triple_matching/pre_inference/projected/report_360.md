# Triple matching report: 360

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Brown | hasAwardReceived | Grammy_Award_for_Best_R_B_Album |
| Little_More_Royalty | hasPerformer | Chris_Brown |

# 2. Unmatched triples

**Total unmatched count: 21**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 21**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Brown | hasAwardReceived | award_bet |
| Chris_Brown | hasAwardReceived | award_billboard_music |
| Chris_Brown | hasAwardReceived | award_soul_train_music |
| Chris_Brown | type | Person |
| Chris_Brown | type | NamedIndividual |
| Chris_Brown | label | "Chris Brown" |
| Grammy_Award_for_Best_R_B_Album | type | Award |
| Grammy_Award_for_Best_R_B_Album | type | NamedIndividual |
| Grammy_Award_for_Best_R_B_Album | label | "Grammy Award" |
| Little_More_Royalty | type | CreativeWork |
| Little_More_Royalty | type | NamedIndividual |
| Little_More_Royalty | label | "Little More (Royalty)" |
| award_bet | type | Award |
| award_bet | type | NamedIndividual |
| award_bet | label | "BET Award" |
| award_billboard_music | type | Award |
| award_billboard_music | type | NamedIndividual |
| award_billboard_music | label | "Billboard Music Award" |
| award_soul_train_music | type | Award |
| award_soul_train_music | type | NamedIndividual |
| award_soul_train_music | label | "Soul Train Music Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 23 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 23 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 21 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.086957 |
| Recall | 1.000000 |
| F1 score | 0.160000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
