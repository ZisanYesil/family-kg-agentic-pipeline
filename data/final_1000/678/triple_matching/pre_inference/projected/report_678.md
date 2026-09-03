# Triple matching report: 678

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Max_Finkelstein | hasBirthDate | "1884-03-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Max_Finkelstein | hasDeathDate | "1940-05-03"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Boyer | hasBirthDate | "1848"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Joseph_Boyer | hasDeathDate | "1930-10-24"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Boyer | hasBirthDate | "1890"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Joseph_Boyer | hasDeathDate | "1924-09-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Joseph_Boyer | type | Person |
| Joseph_Boyer | type | NamedIndividual |
| Joseph_Boyer | label | "Joseph Boyer, Jr." |
| Joseph_Boyer | altLabel | "Joe Boyer" |
| Max_Finkelstein | type | Person |
| Max_Finkelstein | type | NamedIndividual |
| Max_Finkelstein | label | "Max Finkelstein" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.181818 |
| Recall | 0.500000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
