# Triple matching report: 331

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Sweetly_You_ll_Die_Through_Love | hasDirector | Tulio_Demicheli |
| Tulio_Demicheli | hasDeathPlace | Madrid |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Madrid | type | Place |
| Madrid | type | NamedIndividual |
| Madrid | label | "Madrid, Spain" |
| Madrid | altLabel | "Madrid" |
| Sweetly_You_ll_Die_Through_Love | type | Film |
| Sweetly_You_ll_Die_Through_Love | type | NamedIndividual |
| Sweetly_You_ll_Die_Through_Love | label | "Sweetly You'll Die Through Love" |
| Tulio_Demicheli | type | Person |
| Tulio_Demicheli | type | NamedIndividual |
| Tulio_Demicheli | label | "Tulio Demicheli" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
