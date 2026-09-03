# Triple matching report: 326

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Meghan_Trainor | hasAwardReceived | Grammy_Award |
| Watch_Me_Do | hasPerformer | Meghan_Trainor |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Grammy_Award | type | Award |
| Grammy_Award | type | NamedIndividual |
| Grammy_Award | label | "Grammy Award" |
| Meghan_Trainor | hasAwardReceived | ascap_pop_music_award |
| Meghan_Trainor | hasAwardReceived | billboard_music_award |
| Meghan_Trainor | type | Person |
| Meghan_Trainor | type | NamedIndividual |
| Meghan_Trainor | label | "Meghan Trainor" |
| Watch_Me_Do | type | CreativeWork |
| Watch_Me_Do | type | NamedIndividual |
| Watch_Me_Do | label | "Watch Me Do" |
| ascap_pop_music_award | type | Award |
| ascap_pop_music_award | type | NamedIndividual |
| ascap_pop_music_award | label | "ASCAP Pop Music Award" |
| billboard_music_award | type | Award |
| billboard_music_award | type | NamedIndividual |
| billboard_music_award | label | "Billboard Music Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 19 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.105263 |
| Recall | 1.000000 |
| F1 score | 0.190476 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
