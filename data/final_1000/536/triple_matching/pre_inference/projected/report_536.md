# Triple matching report: 536

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Helen_Dortch_Longstreet | hasSpouse | James_Longstreet |
| James_Longstreet | hasEducatedAt | Army |

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
| Army | type | EducationalInstitution |
| Army | type | NamedIndividual |
| Army | label | "United States Military Academy at West Point" |
| Helen_Dortch_Longstreet | type | Person |
| Helen_Dortch_Longstreet | type | NamedIndividual |
| Helen_Dortch_Longstreet | label | "Helen Dortch Longstreet" |
| James_Longstreet | type | Person |
| James_Longstreet | type | NamedIndividual |
| James_Longstreet | label | "James Longstreet" |

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
