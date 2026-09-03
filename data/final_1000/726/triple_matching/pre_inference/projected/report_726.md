# Triple matching report: 726

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Me_and_Liza | hasPerformer | Rufus_Wainwright |
| Rufus_Wainwright | hasParent | Loudon_Wainwright_III |

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
| Loudon_Wainwright_III | type | Person |
| Loudon_Wainwright_III | type | NamedIndividual |
| Loudon_Wainwright_III | label | "Loudon Wainwright III" |
| Me_and_Liza | type | MusicalWork |
| Me_and_Liza | type | NamedIndividual |
| Me_and_Liza | label | "Me and Liza" |
| Rufus_Wainwright | type | Person |
| Rufus_Wainwright | type | NamedIndividual |
| Rufus_Wainwright | label | "Rufus Wainwright" |

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
