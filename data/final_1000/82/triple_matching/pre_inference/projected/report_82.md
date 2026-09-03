# Triple matching report: 82

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| A_M_Julien | hasBirthDate | "1903-07-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| A_M_Julien | hasDeathDate | "2001-01-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ernst_zu_Münster | hasBirthDate | "1766-03-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ernst_zu_Münster | hasDeathDate | "1839-05-20"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| A_M_Julien | type | Person |
| A_M_Julien | type | NamedIndividual |
| A_M_Julien | label | "A.-M. Julien" |
| A_M_Julien | altLabel | "A.- M. Julien" |
| A_M_Julien | altLabel | "A.-M. Julien" |
| A_M_Julien | altLabel | "Aman- Julien Maistre" |
| Ernst_zu_Münster | type | Person |
| Ernst_zu_Münster | type | NamedIndividual |
| Ernst_zu_Münster | label | "Ernst zu Münster" |
| Ernst_zu_Münster | altLabel | "Ernst zu Münster" |
| Ernst_zu_Münster | altLabel | "Graf Ernst Friedrich Herbert zu Münster" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 15 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.266667 |
| Recall | 1.000000 |
| F1 score | 0.421053 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
