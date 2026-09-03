# Triple matching report: 470

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Baby_Face_Morgan | hasProducer | Jack_Schwarz |
| Jack_Schwarz | hasBirthDate | "1896-12-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Seventh_Victim | hasProducer | Val_Lewton |
| Val_Lewton | hasBirthDate | "1904-05-07"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Baby_Face_Morgan | type | Film |
| Baby_Face_Morgan | type | NamedIndividual |
| Baby_Face_Morgan | label | "Baby Face Morgan" |
| Jack_Schwarz | type | Person |
| Jack_Schwarz | type | NamedIndividual |
| Jack_Schwarz | label | "Jack Schwarz" |
| The_Seventh_Victim | type | Film |
| The_Seventh_Victim | type | NamedIndividual |
| The_Seventh_Victim | label | "The Seventh Victim" |
| Val_Lewton | type | Person |
| Val_Lewton | type | NamedIndividual |
| Val_Lewton | label | "Val Lewton" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
