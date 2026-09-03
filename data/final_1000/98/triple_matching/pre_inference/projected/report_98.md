# Triple matching report: 98

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Julius_Rockwell | hasEducatedAt | Yale |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Francis_Williams_Rockwell | hasParent | Julius_Rockwell |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Francis_Williams_Rockwell | type | Person |
| Francis_Williams_Rockwell | type | NamedIndividual |
| Francis_Williams_Rockwell | label | "Francis W. Rockwell" |
| Francis_Williams_Rockwell | altLabel | "Francis Williams Rockwell" |
| Julius_Rockwell | hasParent | Francis_Williams_Rockwell |
| Julius_Rockwell | type | Person |
| Julius_Rockwell | type | NamedIndividual |
| Julius_Rockwell | label | "Julius Rockwell" |
| Yale | type | EducationalInstitution |
| Yale | type | NamedIndividual |
| Yale | label | "Yale University" |
| Yale | altLabel | "Yale" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
