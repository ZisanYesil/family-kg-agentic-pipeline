# Triple matching report: 819

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lasse_Åberg | hasEducatedAt | Konstfack |
| Sällskapsresan_2_Snowroller | hasDirector | Lasse_Åberg |

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
| Konstfack | type | EducationalInstitution |
| Konstfack | type | NamedIndividual |
| Konstfack | label | "Konstfack" |
| Lasse_Åberg | type | Person |
| Lasse_Åberg | type | NamedIndividual |
| Lasse_Åberg | label | "Lasse Åberg" |
| Lasse_Åberg | altLabel | "Lars Gunnar Åberg" |
| Sällskapsresan_2_Snowroller | type | Film |
| Sällskapsresan_2_Snowroller | type | NamedIndividual |
| Sällskapsresan_2_Snowroller | label | "Sällskapsresan 2 – Snowroller" |

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
