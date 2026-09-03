# Triple matching report: 196

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| You_Changed_Me | hasPerformer | Jamie_Foxx |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jamie_Foxx | hasAwardReceived | Best_Actor |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Jamie_Foxx | hasAwardReceived | award_grammy |
| Jamie_Foxx | type | Person |
| Jamie_Foxx | type | NamedIndividual |
| Jamie_Foxx | label | "Jamie Foxx" |
| Jamie_Foxx | altLabel | "Eric Marlon Bishop" |
| You_Changed_Me | type | CreativeWork |
| You_Changed_Me | type | NamedIndividual |
| You_Changed_Me | label | "You Changed Me" |
| award_grammy | type | Award |
| award_grammy | type | NamedIndividual |
| award_grammy | label | "Grammy Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
