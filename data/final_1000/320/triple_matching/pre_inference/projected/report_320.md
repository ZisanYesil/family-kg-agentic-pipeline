# Triple matching report: 320

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_II_the_Strong | hasDeathPlace | Warsaw |
| Maurice_de_Saxe | hasParent | Augustus_II_the_Strong |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_II_the_Strong | hasBirthDate | "1670-05-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| Augustus_II_the_Strong | hasChild | Maurice_de_Saxe |
| Augustus_II_the_Strong | hasDeathDate | "1733-02-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Augustus_II_the_Strong | type | Person |
| Augustus_II_the_Strong | type | NamedIndividual |
| Augustus_II_the_Strong | label | "Augustus II the Strong" |
| Maurice_de_Saxe | hasBirthDate | "1696-10-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Maurice_de_Saxe | hasDeathDate | "1750-11-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Maurice_de_Saxe | type | Person |
| Maurice_de_Saxe | type | NamedIndividual |
| Maurice_de_Saxe | label | "Maurice de Saxe" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
