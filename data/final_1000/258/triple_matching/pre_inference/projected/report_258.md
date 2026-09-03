# Triple matching report: 258

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Margaret_Simey | hasSpouse | Tom_Simey |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Thomas_Spensley_Simey | hasEducatedAt | Balliol_College |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Balliol_College | type | EducationalInstitution |
| Balliol_College | type | NamedIndividual |
| Balliol_College | label | "Balliol College, Oxford" |
| Balliol_College | altLabel | "Balliol College" |
| Margaret_Simey | type | Person |
| Margaret_Simey | type | NamedIndividual |
| Margaret_Simey | label | "Margaret Simey" |
| Margaret_Simey | altLabel | "Margaret Bayne Todd" |
| Tom_Simey | hasEducatedAt | Balliol_College |
| Tom_Simey | type | Person |
| Tom_Simey | type | NamedIndividual |
| Tom_Simey | label | "Tom Simey" |
| Tom_Simey | altLabel | "Thomas Spensley Simey" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
