# Triple matching report: 83

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Princess_Eugénie_of_Greece_and_Denmark | hasParent | Princess_Marie_Bonaparte |
| Princess_Eugénie_of_Greece_and_Denmark | type | Agent |
| Princess_Eugénie_of_Greece_and_Denmark | type | Person |
| Princess_Marie_Bonaparte | hasChild | Princess_Eugénie_of_Greece_and_Denmark |
| Princess_Marie_Bonaparte | hasDeathDate | "1962-09-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| Princess_Marie_Bonaparte | type | Agent |
| Princess_Marie_Bonaparte | type | Person |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Princess_Marie_Bonaparte | hasBirthDate | "1882-07-02"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.875000 |
| Recall | 1.000000 |
| F1 score | 0.933333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
