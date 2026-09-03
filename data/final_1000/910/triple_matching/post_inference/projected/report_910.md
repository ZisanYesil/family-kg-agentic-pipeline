# Triple matching report: 910

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Investors_Chronicle | hasInception | "1860"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Investors_Chronicle | type | Agent |
| Investors_Chronicle | type | Organization |
| The_New_American | hasInception | "1985"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_New_American | type | Agent |
| The_New_American | type | Organization |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| investors_chronicle | hasPublicationDate | "1860"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| investors_chronicle | type | Artifact |
| investors_chronicle | type | CreativeWork |
| the_new_american | hasPublicationDate | "1985"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| the_new_american | type | Artifact |
| the_new_american | type | CreativeWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 0 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 12 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
