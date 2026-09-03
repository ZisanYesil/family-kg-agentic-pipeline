# Triple matching report: 644

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Louis_I | hasParent | Bonne_of_Bohemia |
| Marie_of_Blois_Duchess_of_Anjou | hasSpouse | Louis_I |

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
| Bonne_of_Bohemia | type | Person |
| Bonne_of_Bohemia | type | NamedIndividual |
| Bonne_of_Bohemia | label | "Bonne of Bohemia" |
| Louis_I | type | Person |
| Louis_I | type | NamedIndividual |
| Louis_I | label | "Louis I of Anjou" |
| Marie_of_Blois_Duchess_of_Anjou | type | Person |
| Marie_of_Blois_Duchess_of_Anjou | type | NamedIndividual |
| Marie_of_Blois_Duchess_of_Anjou | label | "Marie of Blois" |

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
