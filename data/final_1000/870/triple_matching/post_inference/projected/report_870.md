# Triple matching report: 870

# 1. Matched triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| A_Gathering_of_Eagles | hasCreator | Delbert_Mann |
| A_Gathering_of_Eagles | hasDirector | Delbert_Mann |
| A_Gathering_of_Eagles | type | Artifact |
| A_Gathering_of_Eagles | type | CreativeWork |
| A_Gathering_of_Eagles | type | Film |
| Delbert_Mann | hasDeathDate | "2007-11-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Delbert_Mann | type | Agent |
| Delbert_Mann | type | Person |
| September_Affair | hasCreator | William_Dieterle |
| September_Affair | hasDirector | William_Dieterle |
| September_Affair | type | Artifact |
| September_Affair | type | CreativeWork |
| September_Affair | type | Film |
| William_Dieterle | hasDeathDate | "1972-12-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Dieterle | type | Agent |
| William_Dieterle | type | Person |

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
| Delbert_Mann | hasBirthDate | "1920-01-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Dieterle | hasBirthDate | "1893-07-15"^^<http://www.w3.org/2001/XMLSchema#date> |

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
