# Triple matching report: 67

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Moscow_Pride_06 | hasPublicationDate | "2006"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Moscow_Pride_06 | type | Artifact |
| Moscow_Pride_06 | type | CreativeWork |
| My_Favourite_Fabric | hasPublicationDate | "2018"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| My_Favourite_Fabric | type | Artifact |
| My_Favourite_Fabric | type | CreativeWork |

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
| Moscow_Pride_06 | type | Film |
| My_Favourite_Fabric | type | Film |

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
