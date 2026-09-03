# Triple matching report: 295

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Lucio_Dalla | hasDeathDate | "2012-03-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lucio_Dalla | type | Agent |
| Lucio_Dalla | type | Person |
| The_Sparrow_s_Fluttering | type | Artifact |
| The_Sparrow_s_Fluttering | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_Sparrow_s_Fluttering | hasComposer | Lucio_Dalla |
| The_Sparrow_s_Fluttering | hasCreator | Lucio_Dalla |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_Sparrow_s_Fluttering | hasPublicationDate | "1988"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Sparrow_s_Fluttering | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 9 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.714286 |
| Recall | 0.714286 |
| F1 score | 0.714286 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
