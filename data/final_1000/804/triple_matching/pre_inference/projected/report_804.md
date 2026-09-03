# Triple matching report: 804

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_II_the_Strong | hasBurialPlace | Wawel_Cathedral |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Maurice_de_Saxe | hasParent | Augustus_II_the_Strong |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_II_the_Strong | hasChild | Maurice_de_Saxe |
| Augustus_II_the_Strong | type | Person |
| Augustus_II_the_Strong | type | NamedIndividual |
| Augustus_II_the_Strong | label | "Augustus II the Strong" |
| Augustus_II_the_Strong | altLabel | "Frederick Augustus I" |
| Maurice_de_Saxe | type | Person |
| Maurice_de_Saxe | type | NamedIndividual |
| Maurice_de_Saxe | label | "Maurice de Saxe" |
| Maurice_de_Saxe | altLabel | "Maurice, Count of Saxony" |
| Wawel_Cathedral | type | Place |
| Wawel_Cathedral | type | NamedIndividual |
| Wawel_Cathedral | label | "Wawel Cathedral" |
| Wawel_Cathedral | altLabel | "Wawel Cathedral in Kraków" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
