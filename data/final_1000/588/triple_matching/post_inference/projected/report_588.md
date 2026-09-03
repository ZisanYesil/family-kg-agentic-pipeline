# Triple matching report: 588

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| James_B_Rhoads | hasBirthPlace | Sioux_City |
| James_B_Rhoads | type | Agent |
| James_B_Rhoads | type | Person |
| Sioux_City | type | Place |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Prologue | hasFounder | James_B_Rhoads |
| Prologue | type | Agent |
| Prologue | type | Organization |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| prologue_magazine | type | Artifact |
| prologue_magazine | type | CreativeWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 9 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.666667 |
| Recall | 0.571429 |
| F1 score | 0.615385 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
