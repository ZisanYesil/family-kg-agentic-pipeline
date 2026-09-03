# Triple matching report: 320

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_II_the_Strong | hasChild | Maurice_de_Saxe |
| Augustus_II_the_Strong | type | Agent |
| Augustus_II_the_Strong | type | Person |
| Maurice_de_Saxe | hasParent | Augustus_II_the_Strong |
| Maurice_de_Saxe | type | Agent |
| Maurice_de_Saxe | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_II_the_Strong | hasDeathPlace | Warsaw |
| Warsaw | type | Place |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_II_the_Strong | hasBirthDate | "1670-05-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| Augustus_II_the_Strong | hasDeathDate | "1733-02-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Maurice_de_Saxe | hasBirthDate | "1696-10-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Maurice_de_Saxe | hasDeathDate | "1750-11-20"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.600000 |
| Recall | 0.750000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
