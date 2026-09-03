# Triple matching report: 405

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Junkin_with_Val_and_Dave | hasCreator | Dave_Bird |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Dave_Bird | hasBirthPlace | Gloucester |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Dave_Bird | type | Person |
| Dave_Bird | type | NamedIndividual |
| Dave_Bird | label | "Dave Bird" |
| Dave_Bird | altLabel | "David Alan \"Dave\" Bird" |
| Junkin_with_Val_and_Dave | type | CreativeWork |
| Junkin_with_Val_and_Dave | type | NamedIndividual |
| Junkin_with_Val_and_Dave | label | "Junkin' with Val and Dave" |

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
