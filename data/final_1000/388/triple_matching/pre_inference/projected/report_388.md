# Triple matching report: 388

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Notorious_B_I_G | hasCauseOfDeath | drive_by_shooting |
| Things_Done_Changed | hasPerformer | Notorious_B_I_G |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Notorious_B_I_G | type | Person |
| Notorious_B_I_G | type | NamedIndividual |
| Notorious_B_I_G | label | "The Notorious B.I.G." |
| Things_Done_Changed | type | CreativeWork |
| Things_Done_Changed | type | NamedIndividual |
| Things_Done_Changed | label | "Things Done Changed" |
| drive_by_shooting | type | CauseOfDeath |
| drive_by_shooting | type | NamedIndividual |
| drive_by_shooting | label | "drive-by shooting" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
