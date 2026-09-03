# Triple matching report: 870

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| A_Gathering_of_Eagles | hasDirector | Delbert_Mann |
| Delbert_Mann | hasDeathDate | "2007-11-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| September_Affair | hasDirector | William_Dieterle |
| William_Dieterle | hasDeathDate | "1972-12-09"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| A_Gathering_of_Eagles | type | Film |
| A_Gathering_of_Eagles | type | NamedIndividual |
| A_Gathering_of_Eagles | label | "A Gathering of Eagles" |
| Delbert_Mann | hasBirthDate | "1920-01-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Delbert_Mann | type | Person |
| Delbert_Mann | type | NamedIndividual |
| Delbert_Mann | label | "Delbert Mann" |
| Delbert_Mann | altLabel | "Delbert Martin Mann Jr." |
| September_Affair | type | Film |
| September_Affair | type | NamedIndividual |
| September_Affair | label | "September Affair" |
| William_Dieterle | hasBirthDate | "1893-07-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Dieterle | type | Person |
| William_Dieterle | type | NamedIndividual |
| William_Dieterle | label | "William Dieterle" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 19 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.210526 |
| Recall | 1.000000 |
| F1 score | 0.347826 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
