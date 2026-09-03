# Triple matching report: 324

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Brown | hasAwardReceived | Grammy_Award_for_Best_R_B_Album |
| Fine_by_Me | hasPerformer | Chris_Brown |

# 2. Unmatched triples

**Total unmatched count: 23**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 23**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Brown | hasAwardReceived | bet_award |
| Chris_Brown | hasAwardReceived | billboard_music_award |
| Chris_Brown | hasAwardReceived | soul_train_award |
| Chris_Brown | type | Person |
| Chris_Brown | type | NamedIndividual |
| Chris_Brown | label | "Chris Brown" |
| Chris_Brown | altLabel | "Christopher Maurice Brown" |
| Fine_by_Me | type | CreativeWork |
| Fine_by_Me | type | NamedIndividual |
| Fine_by_Me | label | "Fine by Me" |
| Fine_by_Me | altLabel | "Fine by Me (Chris Brown song)" |
| Grammy_Award_for_Best_R_B_Album | type | Award |
| Grammy_Award_for_Best_R_B_Album | type | NamedIndividual |
| Grammy_Award_for_Best_R_B_Album | label | "Grammy Award" |
| bet_award | type | Award |
| bet_award | type | NamedIndividual |
| bet_award | label | "BET Award" |
| billboard_music_award | type | Award |
| billboard_music_award | type | NamedIndividual |
| billboard_music_award | label | "Billboard Music Award" |
| soul_train_award | type | Award |
| soul_train_award | type | NamedIndividual |
| soul_train_award | label | "Soul Train Music Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 25 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 25 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 23 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.080000 |
| Recall | 1.000000 |
| F1 score | 0.148148 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
