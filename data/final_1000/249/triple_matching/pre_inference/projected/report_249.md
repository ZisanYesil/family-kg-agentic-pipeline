# Triple matching report: 249

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Clarence_Moore_businessman | hasBirthDate | "1865-03-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Clarence_Moore_businessman | hasDeathDate | "1912-04-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Wilhelmine_Schröder_Devrient | hasBirthDate | "1804-12-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Wilhelmine_Schröder_Devrient | hasDeathDate | "1860-01-26"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Clarence_Moore_businessman | type | Person |
| Clarence_Moore_businessman | type | NamedIndividual |
| Clarence_Moore_businessman | label | "Clarence Moore" |
| Wilhelmine_Schröder_Devrient | type | Person |
| Wilhelmine_Schröder_Devrient | type | NamedIndividual |
| Wilhelmine_Schröder_Devrient | label | "Wilhelmine Schröder-Devrient" |
| Wilhelmine_Schröder_Devrient | altLabel | "Wilhelmine Schröder" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
