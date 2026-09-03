# Triple matching report: 355

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Circle_of_Deception | hasDirector | Jack_Lee |
| Jack_Lee | hasEducatedAt | Marling_School |

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
| Circle_of_Deception | type | Film |
| Circle_of_Deception | type | NamedIndividual |
| Circle_of_Deception | label | "Circle of Deception" |
| Jack_Lee | type | Person |
| Jack_Lee | type | NamedIndividual |
| Jack_Lee | label | "Jack Lee" |
| Marling_School | type | EducationalInstitution |
| Marling_School | type | NamedIndividual |
| Marling_School | label | "Marling School" |

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
