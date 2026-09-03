# Triple matching report: 354

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Prince | hasCountry | American |
| Prince | type | Agent |
| Prince | type | Person |
| When_You_Were_Mine | hasComposer | Prince |
| When_You_Were_Mine | hasCreator | Prince |
| When_You_Were_Mine | type | Artifact |
| When_You_Were_Mine | type | CreativeWork |

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
| When_You_Were_Mine | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 10 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.900000 |
| Recall | 1.000000 |
| F1 score | 0.947368 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
