# Triple matching report: 386

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_Job | type | Artifact |
| The_Job | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Metropolitan_Police_Service | hasCountry | United_Kingdom |
| Metropolitan_Police_Service | type | Agent |
| Metropolitan_Police_Service | type | Organization |
| The_Job | hasPublisher | Metropolitan_Police_Service |
| United_Kingdom | type | Country |
| United_Kingdom | type | Place |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| The_Job | hasPublisher | square_one_publishing |
| square_one_publishing | type | Agent |
| square_one_publishing | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 5 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.400000 |
| Recall | 0.250000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
