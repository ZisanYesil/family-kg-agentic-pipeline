# Triple matching report: 775

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Sam_Cooke | hasDeathPlace | Los_Angeles_California |
| You_Were_Made_for_Me | hasPerformer | Sam_Cooke |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Los_Angeles_California | type | Place |
| Los_Angeles_California | type | NamedIndividual |
| Los_Angeles_California | label | "Los Angeles" |
| Sam_Cooke | type | Person |
| Sam_Cooke | type | NamedIndividual |
| Sam_Cooke | label | "Sam Cooke" |
| Sam_Cooke | altLabel | "Samuel Cook" |
| You_Were_Made_for_Me | type | CreativeWork |
| You_Were_Made_for_Me | type | NamedIndividual |
| You_Were_Made_for_Me | label | "You Were Made for Me" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
