# Triple matching report: 347

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Angel_Eyes_film | hasPublicationDate | "2001"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Angel_Eyes_film | type | Artifact |
| Angel_Eyes_film | type | CreativeWork |
| Mickey_s_Disguises | hasPublicationDate | "1933"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Mickey_s_Disguises | type | Artifact |
| Mickey_s_Disguises | type | CreativeWork |

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
| Angel_Eyes_film | type | Film |
| Mickey_s_Disguises | type | Film |

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
