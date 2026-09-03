# Triple matching report: 984

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fort_Bowie | hasDirector | Howard_W_Koch |
| Howard_W_Koch | hasBirthDate | "1916-04-11"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Fort_Bowie | type | Film |
| Fort_Bowie | type | NamedIndividual |
| Fort_Bowie | label | "Fort Bowie" |
| Howard_W_Koch | type | Person |
| Howard_W_Koch | type | NamedIndividual |
| Howard_W_Koch | label | "Howard W. Koch" |
| Howard_W_Koch | altLabel | "Howard Winchel Koch" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
