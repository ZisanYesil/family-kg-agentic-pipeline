# Triple matching report: 949

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Summer_Skin | hasDirector | Leopoldo_Torre_Nilsson |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Leopoldo_Torre_Nilsson | hasParent | Leopoldo_Torres_Ríos |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Leopoldo_Torre_Nilsson | type | Person |
| Leopoldo_Torre_Nilsson | type | NamedIndividual |
| Leopoldo_Torre_Nilsson | label | "Leopoldo Torre Nilsson" |
| Leopoldo_Torres_Ríos | hasChild | Leopoldo_Torre_Nilsson |
| Leopoldo_Torres_Ríos | type | Person |
| Leopoldo_Torres_Ríos | type | NamedIndividual |
| Leopoldo_Torres_Ríos | label | "Leopoldo Torres Ríos" |
| Summer_Skin | type | Film |
| Summer_Skin | type | NamedIndividual |
| Summer_Skin | label | "Summer Skin" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
