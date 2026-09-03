# Triple matching report: 218

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Damon_Tassos | hasBirthDate | "1923-12-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Damon_Tassos | hasDeathDate | "2001-02-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sir_Frederick_Treves_1st_Baronet | hasBirthDate | "1853-02-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sir_Frederick_Treves_1st_Baronet | hasDeathDate | "1923-12-07"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Damon_Tassos | type | Person |
| Damon_Tassos | type | NamedIndividual |
| Damon_Tassos | label | "Damon Tassos" |
| Sir_Frederick_Treves_1st_Baronet | type | Person |
| Sir_Frederick_Treves_1st_Baronet | type | NamedIndividual |
| Sir_Frederick_Treves_1st_Baronet | label | "Sir Frederick Treves, 1st Baronet" |
| Sir_Frederick_Treves_1st_Baronet | altLabel | "Frederick Treves" |

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
