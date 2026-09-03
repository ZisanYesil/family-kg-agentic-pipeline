# Triple matching report: 497

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Alex_P | hasCountry | Sweden |
| Alex_P | type | Agent |
| Alex_P | type | Person |
| Replay | hasCreator | Alex_P |
| Replay | type | Artifact |
| Replay | type | CreativeWork |
| Sweden | type | Country |
| Sweden | type | Place |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Replay | hasComposer | Alex_P |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Alex_P | hasCountry | greece |
| Replay | type | MusicalWork |
| greece | type | Country |
| greece | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.666667 |
| Recall | 0.888889 |
| F1 score | 0.761905 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
