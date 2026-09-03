# Triple matching report: 667

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Booker_T | hasAwardReceived | WWE_Hall_of_Fame |
| Booker_T | type | Agent |
| Pro_Wrestling_Alliance | hasFounder | Booker_T |
| Pro_Wrestling_Alliance | type | Agent |
| Pro_Wrestling_Alliance | type | Organization |
| WWE_Hall_of_Fame | type | Award |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Booker_T | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 7 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.857143 |
| Recall | 1.000000 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
