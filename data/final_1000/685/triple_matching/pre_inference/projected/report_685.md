# Triple matching report: 685

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mary_Capel_Countess_of_Essex | hasParent | William_Bentinck_1st_Earl_of_Portland |
| William_Bentinck_1st_Earl_of_Portland | hasDeathPlace | Buckinghamshire |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Buckinghamshire | type | Place |
| Buckinghamshire | type | NamedIndividual |
| Buckinghamshire | label | "Bulstrode Park, Buckinghamshire" |
| Mary_Capel_Countess_of_Essex | type | Person |
| Mary_Capel_Countess_of_Essex | type | NamedIndividual |
| Mary_Capel_Countess_of_Essex | label | "Mary Capel, Countess of Essex" |
| William_Bentinck_1st_Earl_of_Portland | type | Person |
| William_Bentinck_1st_Earl_of_Portland | type | NamedIndividual |
| William_Bentinck_1st_Earl_of_Portland | label | "William Bentinck, 1st Earl of Portland" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
