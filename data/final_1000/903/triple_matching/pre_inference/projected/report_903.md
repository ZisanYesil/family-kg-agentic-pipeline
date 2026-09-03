# Triple matching report: 903

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lighter | hasPerformer | Miley_Cyrus |
| Miley_Cyrus | hasParent | Billy_Ray_Cyrus |

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
| Billy_Ray_Cyrus | type | Person |
| Billy_Ray_Cyrus | type | NamedIndividual |
| Billy_Ray_Cyrus | label | "Billy Ray Cyrus" |
| Lighter | type | MusicalWork |
| Lighter | type | NamedIndividual |
| Lighter | label | "Lighter" |
| Miley_Cyrus | type | Person |
| Miley_Cyrus | type | NamedIndividual |
| Miley_Cyrus | label | "Miley Cyrus" |
| Miley_Cyrus | altLabel | "Destiny Hope Cyrus" |
| Miley_Cyrus | altLabel | "Miley Ray Hemsworth" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
