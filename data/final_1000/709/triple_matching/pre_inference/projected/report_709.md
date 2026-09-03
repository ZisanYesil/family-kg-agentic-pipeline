# Triple matching report: 709

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Duke_of_Lower_Lorraine | hasBurialPlace | Basilica_of_Saint_Servatius |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louis_of_Lower_Lorraine | hasParent | Charles_Duke_of_Lower_Lorraine |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Basilica_of_Saint_Servatius | type | Place |
| Basilica_of_Saint_Servatius | type | NamedIndividual |
| Basilica_of_Saint_Servatius | label | "Basilica of Saint Servatius" |
| Basilica_of_Saint_Servatius | altLabel | "Basilica of Saint Servatius" |
| Basilica_of_Saint_Servatius | altLabel | "Basilica of Saint Servatius in Maastricht" |
| Charles_Duke_of_Lower_Lorraine | hasChild | Louis_of_Lower_Lorraine |
| Charles_Duke_of_Lower_Lorraine | type | Person |
| Charles_Duke_of_Lower_Lorraine | type | NamedIndividual |
| Charles_Duke_of_Lower_Lorraine | label | "Charles, Duke of Lower Lorraine" |
| Charles_Duke_of_Lower_Lorraine | altLabel | "Charles, Duke of Lower Lorraine" |
| Louis_of_Lower_Lorraine | type | Person |
| Louis_of_Lower_Lorraine | type | NamedIndividual |
| Louis_of_Lower_Lorraine | label | "Louis of Lower Lorraine" |
| Louis_of_Lower_Lorraine | altLabel | "Louis of Lower Lorraine" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.066667 |
| Recall | 0.500000 |
| F1 score | 0.117647 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
