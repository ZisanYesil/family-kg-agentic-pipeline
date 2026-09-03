# Triple matching report: 415

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gavin_Newsom | hasEducatedAt | Santa_Clara_University |
| Jennifer_Siebel | hasSpouse | Gavin_Newsom |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Gavin_Newsom | type | Person |
| Gavin_Newsom | type | NamedIndividual |
| Gavin_Newsom | label | "Gavin Newsom" |
| Gavin_Newsom | altLabel | "Gavin Christopher Newsom" |
| Jennifer_Siebel | type | Person |
| Jennifer_Siebel | type | NamedIndividual |
| Jennifer_Siebel | label | "Jennifer Siebel Newsom" |
| Jennifer_Siebel | altLabel | "Jennifer Lynn Siebel" |
| Santa_Clara_University | type | EducationalInstitution |
| Santa_Clara_University | type | NamedIndividual |
| Santa_Clara_University | label | "Santa Clara University" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
