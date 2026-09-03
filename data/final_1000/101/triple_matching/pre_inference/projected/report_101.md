# Triple matching report: 101

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Woo | hasCountry | Hong_Kong |
| Mission_Impossible_2 | hasDirector | John_Woo |

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
| Hong_Kong | type | Country |
| Hong_Kong | type | NamedIndividual |
| Hong_Kong | label | "Hong Kong" |
| Hong_Kong | altLabel | "Hong Kong" |
| John_Woo | type | Person |
| John_Woo | type | NamedIndividual |
| John_Woo | label | "John Woo" |
| Mission_Impossible_2 | type | Film |
| Mission_Impossible_2 | type | NamedIndividual |
| Mission_Impossible_2 | label | "Mission: Impossible 2" |

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
