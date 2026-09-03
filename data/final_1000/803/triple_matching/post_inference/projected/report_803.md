# Triple matching report: 803

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Conspirare | type | Agent |
| Conspirare | type | Organization |
| Craig_Hella_Johnson | hasBirthPlace | Crow_Wing_County_Minnesota |
| Craig_Hella_Johnson | type | Agent |
| Craig_Hella_Johnson | type | Person |
| Crow_Wing_County_Minnesota | type | Place |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Conspirare | hasMember | Craig_Hella_Johnson |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Conspirare | hasFounder | Craig_Hella_Johnson |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.857143 |
| Recall | 0.857143 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
