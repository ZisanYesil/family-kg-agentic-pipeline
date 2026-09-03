# Triple matching report: 407

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Omar_Rayo | hasBirthDate | "1928-01-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Omar_Rayo | hasDeathDate | "2010-06-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Stefan_Henze | hasBirthDate | "1981-05-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Stefan_Henze | hasDeathDate | "2016-08-15"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Omar_Rayo | type | Person |
| Omar_Rayo | type | NamedIndividual |
| Omar_Rayo | label | "Omar Rayo" |
| Omar_Rayo | altLabel | "Omar Rayo Reyes" |
| Stefan_Henze | type | Person |
| Stefan_Henze | type | NamedIndividual |
| Stefan_Henze | label | "Stefan Henze" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
