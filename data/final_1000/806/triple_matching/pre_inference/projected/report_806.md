# Triple matching report: 806

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Louis_Armstrong | hasCountry | America |
| When_You_re_Smiling | hasPerformer | Louis_Armstrong |

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
| America | type | Country |
| America | type | NamedIndividual |
| America | label | "United States" |
| America | altLabel | "American" |
| Louis_Armstrong | type | Person |
| Louis_Armstrong | type | NamedIndividual |
| Louis_Armstrong | label | "Louis Armstrong" |
| When_You_re_Smiling | type | CreativeWork |
| When_You_re_Smiling | type | NamedIndividual |
| When_You_re_Smiling | label | "When You're Smiling" |

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
