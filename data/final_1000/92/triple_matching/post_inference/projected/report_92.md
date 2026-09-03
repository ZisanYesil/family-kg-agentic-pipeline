# Triple matching report: 92

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Angel_Square | hasCreator | Anne_Wheeler |
| Angel_Square | hasDirector | Anne_Wheeler |
| Angel_Square | type | Artifact |
| Angel_Square | type | CreativeWork |
| Angel_Square | type | Film |
| Anne_Wheeler | type | Agent |
| Anne_Wheeler | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Wheeler | hasAwardReceived | Officer_of_the_Order_of_Canada |
| Officer_of_the_Order_of_Canada | type | Award |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Wheeler | hasAwardReceived | gemini_award |
| Anne_Wheeler | hasAwardReceived | leo_award |
| gemini_award | type | Award |
| leo_award | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.636364 |
| Recall | 0.777778 |
| F1 score | 0.700000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
