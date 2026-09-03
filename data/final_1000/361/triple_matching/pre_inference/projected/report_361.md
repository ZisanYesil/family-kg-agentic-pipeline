# Triple matching report: 361

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Curtis_Bernhardt | hasBurialPlace | Forest_Lawn_Memorial_Park |
| The_Tunnel | hasDirector | Curtis_Bernhardt |

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
| Curtis_Bernhardt | type | Person |
| Curtis_Bernhardt | type | NamedIndividual |
| Curtis_Bernhardt | label | "Curtis Bernhardt" |
| Forest_Lawn_Memorial_Park | type | Place |
| Forest_Lawn_Memorial_Park | type | NamedIndividual |
| Forest_Lawn_Memorial_Park | label | "Glendale's Forest Lawn Memorial Park Cemetery" |
| Forest_Lawn_Memorial_Park | altLabel | "Forest Lawn Memorial Park Cemetery" |
| The_Tunnel | type | Film |
| The_Tunnel | type | NamedIndividual |
| The_Tunnel | label | "The Tunnel (1933 German-language film)" |
| The_Tunnel | altLabel | "The Tunnel" |

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
