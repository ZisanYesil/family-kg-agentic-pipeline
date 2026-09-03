# Triple matching report: 83

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Princess_Eugénie_of_Greece_and_Denmark | hasParent | Princess_Marie_Bonaparte |
| Princess_Marie_Bonaparte | hasDeathDate | "1962-09-21"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Princess_Eugénie_of_Greece_and_Denmark | type | Person |
| Princess_Eugénie_of_Greece_and_Denmark | type | NamedIndividual |
| Princess_Eugénie_of_Greece_and_Denmark | label | "Princess Eugénie of Greece and Denmark" |
| Princess_Marie_Bonaparte | hasBirthDate | "1882-07-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Princess_Marie_Bonaparte | type | Person |
| Princess_Marie_Bonaparte | type | NamedIndividual |
| Princess_Marie_Bonaparte | label | "Princess Marie Bonaparte" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
