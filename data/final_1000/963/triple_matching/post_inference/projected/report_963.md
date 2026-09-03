# Triple matching report: 963

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Elvira_of_Sicily | type | Agent |
| Elvira_of_Sicily | type | Person |
| John_Count_of_Brienne | type | Agent |
| John_Count_of_Brienne | type | Person |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Elvira_of_Sicily | hasChild | Walter_IV_the_Great_of_Brienne |
| John_Count_of_Brienne | hasParent | Walter_IV_of_Brienne |
| Walter_IV_of_Brienne | hasChild | John_Count_of_Brienne |
| Walter_IV_of_Brienne | type | Agent |
| Walter_IV_of_Brienne | type | Person |
| Walter_IV_the_Great_of_Brienne | hasParent | Elvira_of_Sicily |
| Walter_IV_the_Great_of_Brienne | type | Agent |
| Walter_IV_the_Great_of_Brienne | type | Person |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Elvira_of_Sicily | hasChild | _walter_iv_brienne |
| John_Count_of_Brienne | hasParent | _walter_iv_brienne |
| _walter_iv_brienne | hasChild | John_Count_of_Brienne |
| _walter_iv_brienne | hasParent | Elvira_of_Sicily |
| _walter_iv_brienne | type | Agent |
| _walter_iv_brienne | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 18 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 8 |
| Precision | 0.400000 |
| Recall | 0.333333 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
