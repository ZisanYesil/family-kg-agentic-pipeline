# Triple matching report: 951

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gerald_FitzGerald_3rd_Earl_of_Desmond | hasSibling | Maurice_FitzGerald_2nd_Earl_of_Desmond |
| James_FitzGerald_6th_Earl_of_Desmond | hasParent | Gerald_FitzGerald_3rd_Earl_of_Desmond |

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
| Gerald_FitzGerald_3rd_Earl_of_Desmond | type | Person |
| Gerald_FitzGerald_3rd_Earl_of_Desmond | type | NamedIndividual |
| Gerald_FitzGerald_3rd_Earl_of_Desmond | label | "Gerald FitzGerald, 3rd Earl of Desmond" |
| James_FitzGerald_6th_Earl_of_Desmond | type | Person |
| James_FitzGerald_6th_Earl_of_Desmond | type | NamedIndividual |
| James_FitzGerald_6th_Earl_of_Desmond | label | "James FitzGerald, 6th Earl of Desmond" |
| Maurice_FitzGerald_2nd_Earl_of_Desmond | type | Person |
| Maurice_FitzGerald_2nd_Earl_of_Desmond | type | NamedIndividual |
| Maurice_FitzGerald_2nd_Earl_of_Desmond | label | "Maurice FitzGerald, 2nd Earl of Desmond" |

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
