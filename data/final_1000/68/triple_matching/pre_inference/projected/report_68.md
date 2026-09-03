# Triple matching report: 68

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Princess_Helena_of_Nassau | hasParent | William_Duke_of_Nassau |
| Princess_Marie_of_Waldeck_and_Pyrmont | hasParent | Princess_Helena_of_Nassau |

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
| Princess_Helena_of_Nassau | type | Person |
| Princess_Helena_of_Nassau | type | NamedIndividual |
| Princess_Helena_of_Nassau | label | "Princess Helena of Nassau" |
| Princess_Marie_of_Waldeck_and_Pyrmont | type | Person |
| Princess_Marie_of_Waldeck_and_Pyrmont | type | NamedIndividual |
| Princess_Marie_of_Waldeck_and_Pyrmont | label | "Princess Marie of Waldeck and Pyrmont" |
| Princess_Marie_of_Waldeck_and_Pyrmont | altLabel | "Georgine Henriette Marie" |
| William_Duke_of_Nassau | type | Person |
| William_Duke_of_Nassau | type | NamedIndividual |
| William_Duke_of_Nassau | label | "William, Duke of Nassau" |

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
