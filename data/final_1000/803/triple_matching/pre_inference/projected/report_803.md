# Triple matching report: 803

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Craig_Hella_Johnson | hasBirthPlace | Crow_Wing_County_Minnesota |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Conspirare | hasMember | Craig_Hella_Johnson |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Conspirare | hasFounder | Craig_Hella_Johnson |
| Conspirare | type | Organization |
| Conspirare | type | NamedIndividual |
| Conspirare | label | "Conspirare" |
| Craig_Hella_Johnson | type | Person |
| Craig_Hella_Johnson | type | NamedIndividual |
| Craig_Hella_Johnson | label | "Craig Hella Johnson" |
| Craig_Hella_Johnson | altLabel | "Craig Morris Hella Johnson" |
| Crow_Wing_County_Minnesota | type | Place |
| Crow_Wing_County_Minnesota | type | NamedIndividual |
| Crow_Wing_County_Minnesota | label | "Crow Wing County, Minnesota" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
