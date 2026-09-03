# Triple matching report: 101

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Hong_Kong | type | Country |
| Hong_Kong | type | Place |
| John_Woo | hasCountry | Hong_Kong |
| John_Woo | type | Agent |
| John_Woo | type | Person |
| Mission_Impossible_2 | hasCreator | John_Woo |
| Mission_Impossible_2 | hasDirector | John_Woo |
| Mission_Impossible_2 | type | Artifact |
| Mission_Impossible_2 | type | CreativeWork |
| Mission_Impossible_2 | type | Film |

# 2. Unmatched triples

**Total unmatched count: 0**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 10 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 0 |
| Precision | 1.000000 |
| Recall | 1.000000 |
| F1 score | 1.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
