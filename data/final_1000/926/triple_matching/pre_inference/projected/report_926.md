# Triple matching report: 926

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ante_Babaja | hasDeathDate | "2010-01-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Codine | hasDirector | Henri_Colpi |
| Gold_Frankincense_and_Myrrh | hasDirector | Ante_Babaja |
| Henri_Colpi | hasDeathDate | "2006-01-14"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Ante_Babaja | hasBirthDate | "1927-10-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ante_Babaja | type | Person |
| Ante_Babaja | type | NamedIndividual |
| Ante_Babaja | label | "Ante Babaja" |
| Codine | type | Film |
| Codine | type | NamedIndividual |
| Codine | label | "Codine" |
| Gold_Frankincense_and_Myrrh | type | Film |
| Gold_Frankincense_and_Myrrh | type | NamedIndividual |
| Gold_Frankincense_and_Myrrh | label | "Gold, Frankincense and Myrrh" |
| Henri_Colpi | hasBirthDate | "1921-07-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henri_Colpi | type | Person |
| Henri_Colpi | type | NamedIndividual |
| Henri_Colpi | label | "Henri Colpi" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
