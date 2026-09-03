# Triple matching report: 389

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Sturla_Gunnarsson | hasEmployer | National_Film_Board |
| The_Diary_of_Evelyn_Lau | hasDirector | Sturla_Gunnarsson |

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
| National_Film_Board | type | Organization |
| National_Film_Board | type | NamedIndividual |
| National_Film_Board | label | "National Film Board" |
| Sturla_Gunnarsson | type | Person |
| Sturla_Gunnarsson | type | NamedIndividual |
| Sturla_Gunnarsson | label | "Sturla Gunnarsson" |
| The_Diary_of_Evelyn_Lau | type | Film |
| The_Diary_of_Evelyn_Lau | type | NamedIndividual |
| The_Diary_of_Evelyn_Lau | label | "The Diary Of Evelyn Lau" |

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
