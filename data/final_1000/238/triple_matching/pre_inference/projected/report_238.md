# Triple matching report: 238

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Passion | hasPerformer | Utada_Hikaru |
| Utada_Hikaru | hasParent | Keiko_Fuji |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Keiko_Fuji | type | Person |
| Keiko_Fuji | type | NamedIndividual |
| Keiko_Fuji | label | "Keiko Fuji" |
| Passion | type | MusicalWork |
| Passion | type | NamedIndividual |
| Passion | label | "Passion (Utada Hikaru song)" |
| Passion | altLabel | "Passion" |
| Utada_Hikaru | type | Person |
| Utada_Hikaru | type | NamedIndividual |
| Utada_Hikaru | label | "Utada Hikaru" |
| Utada_Hikaru | altLabel | "Hikaru Utada" |
| Utada_Hikaru | altLabel | "Utada" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
