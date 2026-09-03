# Triple matching report: 678

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Boyer | type | Agent |
| Joseph_Boyer | type | Person |
| Max_Finkelstein | hasBirthDate | "1884-03-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Max_Finkelstein | hasDeathDate | "1940-05-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Max_Finkelstein | type | Agent |
| Max_Finkelstein | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Boyer | hasBirthDate | "1848"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Joseph_Boyer | hasDeathDate | "1930-10-24"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Boyer | hasBirthDate | "1890"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Joseph_Boyer | hasDeathDate | "1924-09-02"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.750000 |
| Recall | 0.750000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
