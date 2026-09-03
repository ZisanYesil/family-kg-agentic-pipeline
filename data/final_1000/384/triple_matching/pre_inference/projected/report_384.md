# Triple matching report: 384

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Amalie_Auguste_of_Bavaria | hasBirthPlace | Munich |
| Princess_Anna_of_Saxony_1836_1859 | hasParent | Amalie_Auguste_of_Bavaria |

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
| Amalie_Auguste_of_Bavaria | type | Person |
| Amalie_Auguste_of_Bavaria | type | NamedIndividual |
| Amalie_Auguste_of_Bavaria | label | "Amalie Auguste of Bavaria" |
| Munich | type | Place |
| Munich | type | NamedIndividual |
| Munich | label | "Munich" |
| Princess_Anna_of_Saxony_1836_1859 | type | Person |
| Princess_Anna_of_Saxony_1836_1859 | type | NamedIndividual |
| Princess_Anna_of_Saxony_1836_1859 | label | "Princess Anna of Saxony (1836–1859)" |

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
