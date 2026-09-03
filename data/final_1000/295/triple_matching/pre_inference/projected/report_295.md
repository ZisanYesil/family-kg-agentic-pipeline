# Triple matching report: 295

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Lucio_Dalla | hasDeathDate | "2012-03-01"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Sparrow_s_Fluttering | hasComposer | Lucio_Dalla |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Lucio_Dalla | type | Person |
| Lucio_Dalla | type | NamedIndividual |
| Lucio_Dalla | label | "Lucio Dalla" |
| The_Sparrow_s_Fluttering | hasPublicationDate | "1988"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Sparrow_s_Fluttering | type | Film |
| The_Sparrow_s_Fluttering | type | NamedIndividual |
| The_Sparrow_s_Fluttering | label | "The Sparrow's Fluttering" |

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
