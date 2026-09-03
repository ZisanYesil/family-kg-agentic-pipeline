# Triple matching report: 817

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Bruno_Mars | hasAwardReceived | Grammy_Award |
| Bruno_Mars | type | Agent |
| Grammy_Award | type | Award |
| Marry_You | hasCreator | Bruno_Mars |
| Marry_You | hasPerformer | Bruno_Mars |
| Marry_You | type | Artifact |
| Marry_You | type | CreativeWork |

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
| Bruno_Mars | type | Person |
| Marry_You | type | MusicalWork |

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
