# Triple matching report: 502

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Toke_also_known_as_Valtoke | hasParent | Gorm_the_Old |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gorm_the_Old | hasDeathPlace | Jelling |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Gorm_the_Old | type | Person |
| Gorm_the_Old | type | NamedIndividual |
| Gorm_the_Old | label | "Gorm the Old" |
| Gorm_the_Old | altLabel | "Gorm the Old" |
| Toke_also_known_as_Valtoke | type | Person |
| Toke_also_known_as_Valtoke | type | NamedIndividual |
| Toke_also_known_as_Valtoke | label | "Valtoke Gormsson" |
| Toke_also_known_as_Valtoke | altLabel | "Toke" |
| Toke_also_known_as_Valtoke | altLabel | "Valtoke Gormsson" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
