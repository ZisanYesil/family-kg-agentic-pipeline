# Triple matching report: 314

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Long_Arm_of_the_Godfather | hasPublicationDate | "1972"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Long_Arm_of_the_Godfather | type | Artifact |
| Long_Arm_of_the_Godfather | type | CreativeWork |
| Virineya | hasPublicationDate | "1968"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Virineya | type | Artifact |
| Virineya | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Long_Arm_of_the_Godfather | type | Film |
| Virineya | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
