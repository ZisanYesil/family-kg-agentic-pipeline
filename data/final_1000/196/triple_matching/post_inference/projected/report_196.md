# Triple matching report: 196

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Jamie_Foxx | type | Agent |
| You_Changed_Me | hasCreator | Jamie_Foxx |
| You_Changed_Me | hasPerformer | Jamie_Foxx |
| You_Changed_Me | type | Artifact |
| You_Changed_Me | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Best_Actor | type | Award |
| Jamie_Foxx | hasAwardReceived | Best_Actor |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Jamie_Foxx | hasAwardReceived | award_grammy |
| Jamie_Foxx | type | Person |
| award_grammy | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 10 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.625000 |
| Recall | 0.714286 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
