# Triple matching report: 326

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Grammy_Award | type | Award |
| Meghan_Trainor | hasAwardReceived | Grammy_Award |
| Meghan_Trainor | type | Agent |
| Watch_Me_Do | hasCreator | Meghan_Trainor |
| Watch_Me_Do | hasPerformer | Meghan_Trainor |
| Watch_Me_Do | type | Artifact |
| Watch_Me_Do | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Meghan_Trainor | hasAwardReceived | ascap_pop_music_award |
| Meghan_Trainor | hasAwardReceived | billboard_music_award |
| Meghan_Trainor | type | Person |
| ascap_pop_music_award | type | Award |
| billboard_music_award | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 12 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.583333 |
| Recall | 1.000000 |
| F1 score | 0.736842 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
