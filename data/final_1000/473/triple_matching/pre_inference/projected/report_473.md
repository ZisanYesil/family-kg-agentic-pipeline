# Triple matching report: 473

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Hans_J_Salter | hasCountry | Austrian |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Thunder_on_the_Hill | hasComposer | Hans_J_Salter |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Austrian | type | Country |
| Austrian | type | NamedIndividual |
| Austrian | label | "Austria" |
| Austrian | altLabel | "Austrian" |
| Hans_J_Salter | hasCountry | united_states |
| Hans_J_Salter | type | Person |
| Hans_J_Salter | type | NamedIndividual |
| Hans_J_Salter | label | "Hans J. Salter" |
| united_states | type | Country |
| united_states | type | NamedIndividual |
| united_states | label | "United States" |
| united_states | altLabel | "American" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
