# Triple matching report: 376

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bellingham_Review | hasPublisher | Western_Washington_University |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Western_Washington_University | hasInception | "1893"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Bellingham_Review | type | CreativeWork |
| Bellingham_Review | type | NamedIndividual |
| Bellingham_Review | label | "Bellingham Review" |
| Western_Washington_University | hasInception | "1886"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Western_Washington_University | type | Organization |
| Western_Washington_University | type | NamedIndividual |
| Western_Washington_University | label | "Western Washington University" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
