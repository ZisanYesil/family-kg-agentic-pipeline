# Triple matching report: 814

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Bernadine | hasCreator | Pat_Boone |
| Bernadine | hasPerformer | Pat_Boone |
| Bernadine | type | Artifact |
| Bernadine | type | CreativeWork |
| Gospel_Music_Hall_of_Fame | type | Award |
| Pat_Boone | hasAwardReceived | Gospel_Music_Hall_of_Fame |
| Pat_Boone | type | Agent |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bernadine | type | MusicalWork |
| Pat_Boone | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 9 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.777778 |
| Recall | 1.000000 |
| F1 score | 0.875000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
