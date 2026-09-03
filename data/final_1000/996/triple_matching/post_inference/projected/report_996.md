# Triple matching report: 996

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | type | Agent |
| Max_Ophüls | type | Person |
| There_s_No_Tomorrow | hasCreator | Max_Ophüls |
| There_s_No_Tomorrow | hasDirector | Max_Ophüls |
| There_s_No_Tomorrow | type | Artifact |
| There_s_No_Tomorrow | type | CreativeWork |
| There_s_No_Tomorrow | type | Film |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasBirthPlace | Saarbrücken |
| Saarbrücken | type | Place |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasBirthPlace | country_germany |
| country_germany | type | Country |
| country_germany | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.700000 |
| Recall | 0.777778 |
| F1 score | 0.736842 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
