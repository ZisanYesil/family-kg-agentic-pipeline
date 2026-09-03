# Triple matching report: 268

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mario_Laserna_Pinzón | hasBirthPlace | Paris |
| The_University_of_Los_Andes | hasFounder | Mario_Laserna_Pinzón |

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
| Mario_Laserna_Pinzón | type | Person |
| Mario_Laserna_Pinzón | type | NamedIndividual |
| Mario_Laserna_Pinzón | label | "Mario Laserna Pinzón" |
| Paris | type | Place |
| Paris | type | NamedIndividual |
| Paris | label | "Paris" |
| The_University_of_Los_Andes | type | Organization |
| The_University_of_Los_Andes | type | NamedIndividual |
| The_University_of_Los_Andes | label | "University of Los Andes (Colombia)" |

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
