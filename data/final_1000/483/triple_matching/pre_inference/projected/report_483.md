# Triple matching report: 483

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| José_González_Ganoza | hasBirthDate | "1954-07-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| José_González_Ganoza | hasDeathDate | "1987-12-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sir_Walter_Boyd_1st_Baronet | hasBirthDate | "1833-01-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sir_Walter_Boyd_1st_Baronet | hasDeathDate | "1918-06-25"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| José_González_Ganoza | type | Person |
| José_González_Ganoza | type | NamedIndividual |
| José_González_Ganoza | label | "José González Ganoza" |
| Sir_Walter_Boyd_1st_Baronet | type | Person |
| Sir_Walter_Boyd_1st_Baronet | type | NamedIndividual |
| Sir_Walter_Boyd_1st_Baronet | label | "Sir Walter Boyd, 1st Baronet" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
