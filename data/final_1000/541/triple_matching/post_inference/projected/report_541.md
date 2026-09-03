# Triple matching report: 541

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Drugstore_Cowboy | hasPublicationDate | "1989"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Drugstore_Cowboy | type | Artifact |
| Drugstore_Cowboy | type | CreativeWork |
| When_the_Sea_Rises | hasPublicationDate | "2004"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| When_the_Sea_Rises | type | Artifact |
| When_the_Sea_Rises | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Drugstore_Cowboy | type | Film |
| When_the_Sea_Rises | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
