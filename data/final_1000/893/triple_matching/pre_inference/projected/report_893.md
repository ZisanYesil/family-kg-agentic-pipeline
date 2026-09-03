# Triple matching report: 893

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| A_Very_Moral_Night | hasDirector | Károly_Makk |
| Károly_Makk | hasBirthPlace | Berettyóújfalu |

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
| A_Very_Moral_Night | type | Film |
| A_Very_Moral_Night | type | NamedIndividual |
| A_Very_Moral_Night | label | "A Very Moral Night" |
| Berettyóújfalu | type | Place |
| Berettyóújfalu | type | NamedIndividual |
| Berettyóújfalu | label | "Berettyóújfalu" |
| Károly_Makk | type | Person |
| Károly_Makk | type | NamedIndividual |
| Károly_Makk | label | "Károly Makk" |

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
