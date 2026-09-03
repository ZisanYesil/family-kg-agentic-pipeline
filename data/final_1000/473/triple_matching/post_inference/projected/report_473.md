# Triple matching report: 473

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Austrian | type | Country |
| Austrian | type | Place |
| Hans_J_Salter | hasCountry | Austrian |
| Hans_J_Salter | type | Agent |
| Hans_J_Salter | type | Person |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Thunder_on_the_Hill | hasComposer | Hans_J_Salter |
| Thunder_on_the_Hill | hasCreator | Hans_J_Salter |
| Thunder_on_the_Hill | type | Artifact |
| Thunder_on_the_Hill | type | CreativeWork |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Hans_J_Salter | hasCountry | united_states |
| united_states | type | Country |
| united_states | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.625000 |
| Recall | 0.555556 |
| F1 score | 0.588235 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
