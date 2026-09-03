# Triple matching report: 387

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Linton | hasSpouse | Steven_Mnuchin |
| Louise_Linton | type | Agent |
| Louise_Linton | type | Person |
| Steven_Mnuchin | hasSpouse | Louise_Linton |
| Steven_Mnuchin | type | Agent |
| Steven_Mnuchin | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Goldman | type | Agent |
| Goldman | type | Organization |
| Steven_Mnuchin | hasEmployer | Goldman |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Steven_Mnuchin | hasEmployer | us_treasury_department |
| us_treasury_department | type | Agent |
| us_treasury_department | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.666667 |
| Recall | 0.666667 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
