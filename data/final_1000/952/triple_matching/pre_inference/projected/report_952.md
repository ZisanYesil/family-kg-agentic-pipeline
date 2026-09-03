# Triple matching report: 952

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Husayn_ibn_Ali | hasCauseOfDeath | Battle_of_Karbala |
| Ruqayyah_bint_Husayn | hasParent | Husayn_ibn_Ali |

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
| Battle_of_Karbala | type | CauseOfDeath |
| Battle_of_Karbala | type | NamedIndividual |
| Battle_of_Karbala | label | "killed in the Battle of Karbala" |
| Husayn_ibn_Ali | type | Person |
| Husayn_ibn_Ali | type | NamedIndividual |
| Husayn_ibn_Ali | label | "Husayn ibn Ali" |
| Ruqayyah_bint_Husayn | type | Person |
| Ruqayyah_bint_Husayn | type | NamedIndividual |
| Ruqayyah_bint_Husayn | label | "Ruqayyah bint Al-Ḥusayn" |

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
