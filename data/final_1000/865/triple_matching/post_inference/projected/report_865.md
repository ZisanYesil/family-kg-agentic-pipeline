# Triple matching report: 865

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Fernando_Cortés | hasSpouse | Mapy_Cortés |
| Fernando_Cortés | type | Agent |
| Fernando_Cortés | type | Person |
| Mapy_Cortés | hasSpouse | Fernando_Cortés |
| Mapy_Cortés | type | Agent |
| Mapy_Cortés | type | Person |
| My_Three_Merry_Widows | hasCreator | Fernando_Cortés |
| My_Three_Merry_Widows | hasDirector | Fernando_Cortés |
| My_Three_Merry_Widows | type | Artifact |
| My_Three_Merry_Widows | type | CreativeWork |
| My_Three_Merry_Widows | type | Film |

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
| Fernando_Cortés | hasBirthDate | "1909-10-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Fernando_Cortés | hasDeathDate | "1979"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 13 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.846154 |
| Recall | 1.000000 |
| F1 score | 0.916667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
