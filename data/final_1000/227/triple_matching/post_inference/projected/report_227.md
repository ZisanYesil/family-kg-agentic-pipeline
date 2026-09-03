# Triple matching report: 227

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| The_Man_in_Grey | hasPublicationDate | "1943"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Man_in_Grey | type | Artifact |
| The_Man_in_Grey | type | CreativeWork |
| The_Queen_s_Traitor | hasPublicationDate | "1967"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Queen_s_Traitor | type | Artifact |
| The_Queen_s_Traitor | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Man_in_Grey | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 7 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.857143 |
| Recall | 1.000000 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
