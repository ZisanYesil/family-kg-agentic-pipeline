# Triple matching report: 863

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Louis_Count_of_Verdun | hasParent | Otto_I_Count_of_Chiny |
| Otto_I_Count_of_Chiny | hasParent | Gerberge_of_Lorraine |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Gerberge_of_Lorraine | type | Person |
| Gerberge_of_Lorraine | type | NamedIndividual |
| Gerberge_of_Lorraine | label | "Gerberge of Lorraine" |
| Louis_Count_of_Verdun | type | Person |
| Louis_Count_of_Verdun | type | NamedIndividual |
| Louis_Count_of_Verdun | label | "Louis I, Count of Verdun" |
| Louis_Count_of_Verdun | altLabel | "Louis I" |
| Otto_I_Count_of_Chiny | type | Person |
| Otto_I_Count_of_Chiny | type | NamedIndividual |
| Otto_I_Count_of_Chiny | label | "Otto I, Count of Chiny" |
| Otto_I_Count_of_Chiny | altLabel | "Otto I" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
