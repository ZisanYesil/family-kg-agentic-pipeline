# Triple matching report: 470

# 1. Matched triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Baby_Face_Morgan | hasProducer | Jack_Schwarz |
| Baby_Face_Morgan | type | Artifact |
| Baby_Face_Morgan | type | CreativeWork |
| Jack_Schwarz | hasBirthDate | "1896-12-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jack_Schwarz | type | Agent |
| Jack_Schwarz | type | Person |
| The_Seventh_Victim | hasProducer | Val_Lewton |
| The_Seventh_Victim | type | Artifact |
| The_Seventh_Victim | type | CreativeWork |
| Val_Lewton | hasBirthDate | "1904-05-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Val_Lewton | type | Agent |
| Val_Lewton | type | Person |

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
| Baby_Face_Morgan | type | Film |
| The_Seventh_Victim | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 12 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.857143 |
| Recall | 1.000000 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
