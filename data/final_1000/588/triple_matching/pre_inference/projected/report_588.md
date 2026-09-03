# Triple matching report: 588

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| James_B_Rhoads | hasBirthPlace | Sioux_City |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Prologue | hasFounder | James_B_Rhoads |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| James_B_Rhoads | type | Person |
| James_B_Rhoads | type | NamedIndividual |
| James_B_Rhoads | label | "James B. Rhoads" |
| Sioux_City | type | Place |
| Sioux_City | type | NamedIndividual |
| Sioux_City | label | "Sioux City, Iowa" |
| prologue_magazine | type | CreativeWork |
| prologue_magazine | type | NamedIndividual |
| prologue_magazine | label | "Prologue (magazine)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
