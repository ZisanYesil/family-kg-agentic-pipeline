# Triple matching report: 926

# 1. Matched triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Ante_Babaja | hasDeathDate | "2010-01-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ante_Babaja | type | Agent |
| Ante_Babaja | type | Person |
| Codine | hasCreator | Henri_Colpi |
| Codine | hasDirector | Henri_Colpi |
| Codine | type | Artifact |
| Codine | type | CreativeWork |
| Codine | type | Film |
| Gold_Frankincense_and_Myrrh | hasCreator | Ante_Babaja |
| Gold_Frankincense_and_Myrrh | hasDirector | Ante_Babaja |
| Gold_Frankincense_and_Myrrh | type | Artifact |
| Gold_Frankincense_and_Myrrh | type | CreativeWork |
| Gold_Frankincense_and_Myrrh | type | Film |
| Henri_Colpi | hasDeathDate | "2006-01-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henri_Colpi | type | Agent |
| Henri_Colpi | type | Person |

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
| Ante_Babaja | hasBirthDate | "1927-10-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henri_Colpi | hasBirthDate | "1921-07-15"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 16 |
| Union triples in scope | 18 |
| True positives (matched) | 16 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.888889 |
| Recall | 1.000000 |
| F1 score | 0.941176 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
