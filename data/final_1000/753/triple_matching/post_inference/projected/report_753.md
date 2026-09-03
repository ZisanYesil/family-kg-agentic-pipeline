# Triple matching report: 753

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Jefery_Levy | hasEmployer | University_of_Southern_California |
| Jefery_Levy | type | Agent |
| Jefery_Levy | type | Person |
| Man_of_God | hasCreator | Jefery_Levy |
| Man_of_God | hasDirector | Jefery_Levy |
| Man_of_God | type | Artifact |
| Man_of_God | type | CreativeWork |
| Man_of_God | type | Film |
| University_of_Southern_California | type | Agent |
| University_of_Southern_California | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| University_of_Southern_California | type | EducationalInstitution |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 11 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.909091 |
| Recall | 1.000000 |
| F1 score | 0.952381 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
