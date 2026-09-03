# Triple matching report: 872

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Sol_Niger_Within | type | Artifact |
| Sol_Niger_Within | type | CreativeWork |
| The_Magic_Place | hasPublicationDate | "2011-02-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Magic_Place | type | Artifact |
| The_Magic_Place | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sol_Niger_Within | hasPublicationDate | "1999"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sol_Niger_Within | hasPublicationDate | "1997"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 7 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.833333 |
| Recall | 0.833333 |
| F1 score | 0.833333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
