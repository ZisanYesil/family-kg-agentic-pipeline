# Triple matching report: 934

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Jack_the_Bear | hasPublicationDate | "1993"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Jack_the_Bear | type | Artifact |
| Jack_the_Bear | type | CreativeWork |
| Nattukku_Oru_Nallavan | hasPublicationDate | "1991"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Nattukku_Oru_Nallavan | type | Artifact |
| Nattukku_Oru_Nallavan | type | CreativeWork |

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
| Jack_the_Bear | type | Film |
| Nattukku_Oru_Nallavan | type | Film |

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
