# Triple matching report: 186

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| His_Name_Was_Holy_Ghost | hasCountry | Italian |
| His_Name_Was_Holy_Ghost | type | Artifact |
| Italian | type | Country |
| Italian | type | Place |
| The_Cop_in_Blue_Jeans | hasCountry | Italian |
| The_Cop_in_Blue_Jeans | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| His_Name_Was_Holy_Ghost | hasCountry | Spanish |
| Spanish | type | Country |
| Spanish | type | Place |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| His_Name_Was_Holy_Ghost | type | CreativeWork |
| His_Name_Was_Holy_Ghost | type | Film |
| The_Cop_in_Blue_Jeans | type | CreativeWork |
| The_Cop_in_Blue_Jeans | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.600000 |
| Recall | 0.666667 |
| F1 score | 0.631579 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
