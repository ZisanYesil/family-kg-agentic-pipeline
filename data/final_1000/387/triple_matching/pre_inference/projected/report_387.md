# Triple matching report: 387

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Linton | hasSpouse | Steven_Mnuchin |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Steven_Mnuchin | hasEmployer | Goldman |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Linton | type | Person |
| Louise_Linton | type | NamedIndividual |
| Louise_Linton | label | "Louise Linton" |
| Steven_Mnuchin | hasEmployer | us_treasury_department |
| Steven_Mnuchin | type | Person |
| Steven_Mnuchin | type | NamedIndividual |
| Steven_Mnuchin | label | "Steven Mnuchin" |
| us_treasury_department | type | Organization |
| us_treasury_department | type | NamedIndividual |
| us_treasury_department | label | "United States Department of the Treasury" |
| us_treasury_department | altLabel | "U.S. Treasury" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
