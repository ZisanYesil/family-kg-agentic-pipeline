# Triple matching report: 39

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_Winkelmann | hasEmployer | Dortmund_University_of_Applied_Sciences_and_Arts |
| Adolf_Winkelmann | type | Agent |
| Adolf_Winkelmann | type | Person |
| Die_Abfahrer | hasCreator | Adolf_Winkelmann |
| Die_Abfahrer | hasDirector | Adolf_Winkelmann |
| Die_Abfahrer | type | Artifact |
| Die_Abfahrer | type | CreativeWork |
| Die_Abfahrer | type | Film |
| Dortmund_University_of_Applied_Sciences_and_Arts | type | Agent |
| Dortmund_University_of_Applied_Sciences_and_Arts | type | Organization |

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
| Dortmund_University_of_Applied_Sciences_and_Arts | type | EducationalInstitution |

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
