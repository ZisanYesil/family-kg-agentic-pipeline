# Triple matching report: 14

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| George_Albert_Smith | type | Agent |
| George_Albert_Smith | type | Person |
| Old_Man_Drinking_a_Glass_of_Beer | hasCreator | George_Albert_Smith |
| Old_Man_Drinking_a_Glass_of_Beer | hasDirector | George_Albert_Smith |
| Old_Man_Drinking_a_Glass_of_Beer | type | Artifact |
| Old_Man_Drinking_a_Glass_of_Beer | type | CreativeWork |
| Old_Man_Drinking_a_Glass_of_Beer | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Brighton | type | Place |
| George_Albert_Smith | hasDeathPlace | Brighton |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| George_Albert_Smith | hasBirthDate | "1864-01-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_Albert_Smith | hasDeathDate | "1959-05-17"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.777778 |
| Recall | 0.777778 |
| F1 score | 0.777778 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
