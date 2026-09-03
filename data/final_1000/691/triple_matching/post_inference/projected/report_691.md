# Triple matching report: 691

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Kirk_Douglas | hasBirthDate | "1916-12-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Kirk_Douglas | type | Agent |
| Kirk_Douglas | type | Person |
| Sidney_Franklin | type | Agent |
| The_Indian_Fighter | hasProducer | Kirk_Douglas |
| The_Indian_Fighter | type | Artifact |
| The_Indian_Fighter | type | CreativeWork |
| The_Story_of_Three_Loves | hasProducer | Sidney_Franklin |
| The_Story_of_Three_Loves | type | Artifact |
| The_Story_of_Three_Loves | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Sidney_Franklin_director | hasBirthDate | "1893-03-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sidney_Franklin_director | type | Agent |
| Sidney_Franklin_director | type | Person |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Sidney_Franklin | hasBirthDate | "1893-03-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sidney_Franklin | hasDeathDate | "1972-05-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sidney_Franklin | type | Person |
| The_Indian_Fighter | hasPublicationDate | "1955"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Indian_Fighter | type | Film |
| The_Story_of_Three_Loves | hasPublicationDate | "1953"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Story_of_Three_Loves | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 13 |
| Union triples in scope | 20 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.588235 |
| Recall | 0.769231 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
