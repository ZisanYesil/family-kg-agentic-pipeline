# Triple matching report: 664

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Henry_Dow | hasEducatedAt | Case |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Alden_B_Dow | hasParent | Herbert_Henry_Dow |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Alden_B_Dow | type | Person |
| Alden_B_Dow | type | NamedIndividual |
| Alden_B_Dow | label | "Alden B. Dow" |
| Case | type | EducationalInstitution |
| Case | type | NamedIndividual |
| Case | label | "Case School of Applied Science" |
| Herbert_Henry_Dow | hasParent | Alden_B_Dow |
| Herbert_Henry_Dow | type | Person |
| Herbert_Henry_Dow | type | NamedIndividual |
| Herbert_Henry_Dow | label | "Herbert Henry Dow" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
