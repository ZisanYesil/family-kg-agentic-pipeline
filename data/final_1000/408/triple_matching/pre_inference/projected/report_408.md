# Triple matching report: 408

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Masters | hasCountry | British |
| Metropolitan | hasMember | John_Masters |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "British" |
| John_Masters | type | Person |
| John_Masters | type | NamedIndividual |
| John_Masters | label | "John Masters" |
| Metropolitan | type | Organization |
| Metropolitan | type | NamedIndividual |
| Metropolitan | label | "Metropolitan" |
| Metropolitan | altLabel | "Metropolitan (band)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
