# Triple matching report: 691

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Kirk_Douglas | hasBirthDate | "1916-12-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Indian_Fighter | hasProducer | Kirk_Douglas |
| The_Story_of_Three_Loves | hasProducer | Sidney_Franklin |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sidney_Franklin_director | hasBirthDate | "1893-03-21"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Kirk_Douglas | type | Person |
| Kirk_Douglas | type | NamedIndividual |
| Kirk_Douglas | label | "Kirk Douglas" |
| Sidney_Franklin | hasBirthDate | "1893-03-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sidney_Franklin | hasDeathDate | "1972-05-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sidney_Franklin | type | Person |
| Sidney_Franklin | type | NamedIndividual |
| Sidney_Franklin | label | "Sidney Franklin" |
| The_Indian_Fighter | hasPublicationDate | "1955"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Indian_Fighter | type | Film |
| The_Indian_Fighter | type | NamedIndividual |
| The_Indian_Fighter | label | "The Indian Fighter" |
| The_Story_of_Three_Loves | hasPublicationDate | "1953"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Story_of_Three_Loves | type | Film |
| The_Story_of_Three_Loves | type | NamedIndividual |
| The_Story_of_Three_Loves | label | "The Story Of Three Loves" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.157895 |
| Recall | 0.750000 |
| F1 score | 0.260870 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
