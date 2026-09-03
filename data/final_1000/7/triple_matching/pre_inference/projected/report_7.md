# Triple matching report: 7

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| God | hasPerformer | John_Lennon |
| John_Lennon | hasBirthPlace | Liverpool |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| God | type | CreativeWork |
| God | type | NamedIndividual |
| God | label | "God" |
| John_Lennon | type | Person |
| John_Lennon | type | NamedIndividual |
| John_Lennon | label | "John Lennon" |
| Liverpool | type | Place |
| Liverpool | type | NamedIndividual |
| Liverpool | label | "Liverpool" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
