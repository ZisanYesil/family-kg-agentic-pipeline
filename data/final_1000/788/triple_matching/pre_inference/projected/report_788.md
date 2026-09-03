# Triple matching report: 788

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ryu_Mi_yong | hasBirthDate | "1921-02-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ryu_Mi_yong | hasDeathDate | "2016-11-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Thomas_Johannes_Lauritz_Parr | hasBirthDate | "1862-05-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Thomas_Johannes_Lauritz_Parr | hasDeathDate | "1935-08-12"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Ryu_Mi_yong | type | Person |
| Ryu_Mi_yong | type | NamedIndividual |
| Ryu_Mi_yong | label | "Ryu Mi-yong" |
| Thomas_Johannes_Lauritz_Parr | type | Person |
| Thomas_Johannes_Lauritz_Parr | type | NamedIndividual |
| Thomas_Johannes_Lauritz_Parr | label | "Thomas Johannes Lauritz Parr" |

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
