# Triple matching report: 224

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Wheatstone | hasBirthDate | "1802-02-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Charles_Wheatstone | hasDeathDate | "1875-10-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_Claude_Lauzon | hasBirthDate | "1953-09-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_Claude_Lauzon | hasDeathDate | "1997-08-10"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Wheatstone | type | Person |
| Charles_Wheatstone | type | NamedIndividual |
| Charles_Wheatstone | label | "Charles Wheatstone" |
| Jean_Claude_Lauzon | type | Person |
| Jean_Claude_Lauzon | type | NamedIndividual |
| Jean_Claude_Lauzon | label | "Jean-Claude Lauzon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
