# Triple matching report: 872

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Magic_Place | hasPublicationDate | "2011-02-21"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sol_Niger_Within | hasPublicationDate | "1999"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Sol_Niger_Within | hasPublicationDate | "1997"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Sol_Niger_Within | type | CreativeWork |
| Sol_Niger_Within | type | NamedIndividual |
| Sol_Niger_Within | label | "Sol Niger Within" |
| The_Magic_Place | type | CreativeWork |
| The_Magic_Place | type | NamedIndividual |
| The_Magic_Place | label | "The Magic Place" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
