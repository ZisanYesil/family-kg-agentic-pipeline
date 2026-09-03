# Triple matching report: 221

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Horror_Story_film | hasPublicationDate | "2013-09-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Horror_Story_film | type | Artifact |
| Horror_Story_film | type | CreativeWork |
| The_Heat_s_On | hasPublicationDate | "1943"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Heat_s_On | type | Artifact |
| The_Heat_s_On | type | CreativeWork |

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
| Horror_Story_film | type | Film |
| The_Heat_s_On | type | Film |

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
