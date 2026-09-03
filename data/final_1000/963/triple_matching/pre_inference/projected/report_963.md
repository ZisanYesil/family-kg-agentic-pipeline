# Triple matching report: 963

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Count_of_Brienne | hasParent | Walter_IV_of_Brienne |
| Walter_IV_the_Great_of_Brienne | hasParent | Elvira_of_Sicily |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Elvira_of_Sicily | type | Person |
| Elvira_of_Sicily | type | NamedIndividual |
| Elvira_of_Sicily | label | "Elvira of Sicily" |
| John_Count_of_Brienne | hasParent | _walter_iv_brienne |
| John_Count_of_Brienne | type | Person |
| John_Count_of_Brienne | type | NamedIndividual |
| John_Count_of_Brienne | label | "John, Count of Brienne" |
| _walter_iv_brienne | hasParent | Elvira_of_Sicily |
| _walter_iv_brienne | type | Person |
| _walter_iv_brienne | type | NamedIndividual |
| _walter_iv_brienne | label | "Walter IV, Count of Brienne" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
