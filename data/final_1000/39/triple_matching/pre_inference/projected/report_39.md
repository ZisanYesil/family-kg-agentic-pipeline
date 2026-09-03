# Triple matching report: 39

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Die_Abfahrer | hasDirector | Adolf_Winkelmann |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_Winkelmann | hasEmployer | Dortmund_University_of_Applied_Sciences_and_Arts |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_Winkelmann | type | Person |
| Adolf_Winkelmann | type | NamedIndividual |
| Adolf_Winkelmann | label | "Adolf Winkelmann" |
| Die_Abfahrer | type | Film |
| Die_Abfahrer | type | NamedIndividual |
| Die_Abfahrer | label | "Die Abfahrer" |
| Dortmund_University_of_Applied_Sciences_and_Arts | type | EducationalInstitution |
| Dortmund_University_of_Applied_Sciences_and_Arts | type | NamedIndividual |
| Dortmund_University_of_Applied_Sciences_and_Arts | label | "Dortmund University of Applied Sciences and Arts" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
