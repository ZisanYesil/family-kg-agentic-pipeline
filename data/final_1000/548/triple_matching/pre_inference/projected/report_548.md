# Triple matching report: 548

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Henry_Wright | hasEducatedAt | Dartmouth |
| Mary_Tappan_Wright | hasSpouse | John_Henry_Wright |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Dartmouth | type | EducationalInstitution |
| Dartmouth | type | NamedIndividual |
| Dartmouth | label | "Dartmouth College" |
| John_Henry_Wright | type | Person |
| John_Henry_Wright | type | NamedIndividual |
| John_Henry_Wright | label | "John Henry Wright" |
| Mary_Tappan_Wright | type | Person |
| Mary_Tappan_Wright | type | NamedIndividual |
| Mary_Tappan_Wright | label | "Mary Tappan Wright" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
