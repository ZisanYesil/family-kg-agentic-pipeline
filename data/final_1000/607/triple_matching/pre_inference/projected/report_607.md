# Triple matching report: 607

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Kellam_Tylee | hasBirthDate | "1887-04-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_Kellam_Tylee | hasDeathDate | "1961-04-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| James_A_Ryder | hasBirthDate | "1800-10-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| James_A_Ryder | hasDeathDate | "1860-01-12"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Kellam_Tylee | type | Person |
| Arthur_Kellam_Tylee | type | NamedIndividual |
| Arthur_Kellam_Tylee | label | "Arthur Kellam Tylee" |
| Arthur_Kellam_Tylee | altLabel | "Arthur Kellam Tylee" |
| James_A_Ryder | type | Person |
| James_A_Ryder | type | NamedIndividual |
| James_A_Ryder | label | "James A. Ryder" |
| James_A_Ryder | altLabel | "James A. Ryder" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.333333 |
| Recall | 1.000000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
