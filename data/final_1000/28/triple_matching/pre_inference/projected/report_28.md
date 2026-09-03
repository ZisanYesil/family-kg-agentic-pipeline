# Triple matching report: 28

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Duchess_Maria_Dorothea_of_Württemberg | hasParent | Duke_Louis_of_Württemberg |
| Duke_Louis_of_Württemberg | hasDeathPlace | Kirchheim_unter_Teck |

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
| Duchess_Maria_Dorothea_of_Württemberg | type | Person |
| Duchess_Maria_Dorothea_of_Württemberg | type | NamedIndividual |
| Duchess_Maria_Dorothea_of_Württemberg | label | "Duchess Maria Dorothea of Württemberg" |
| Duchess_Maria_Dorothea_of_Württemberg | altLabel | "Maria Dorothea Luise Wilhelmine Caroline" |
| Duke_Louis_of_Württemberg | type | Person |
| Duke_Louis_of_Württemberg | type | NamedIndividual |
| Duke_Louis_of_Württemberg | label | "Duke Louis of Württemberg" |
| Duke_Louis_of_Württemberg | altLabel | "Louis Friedrich Alexander" |
| Kirchheim_unter_Teck | type | Place |
| Kirchheim_unter_Teck | type | NamedIndividual |
| Kirchheim_unter_Teck | label | "Kirchheim unter Teck" |

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
