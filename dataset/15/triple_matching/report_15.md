# Triple matching report: 15

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Q303 | hasBurialPlace | Q545360 |
| Q303 | type | Agent |
| Q303 | type | Person |
| Q545360 | type | Place |
| Q7782748 | hasCreator | Q303 |
| Q7782748 | hasPerformer | Q303 |
| Q7782748 | type | Artifact |
| Q7782748 | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Q303 | hasBirthDate | "1935-01-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q303 | hasDeathDate | "1977-08-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q7782748 | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 11 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.727273 |
| Recall | 1.000000 |
| F1 score | 0.842105 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
