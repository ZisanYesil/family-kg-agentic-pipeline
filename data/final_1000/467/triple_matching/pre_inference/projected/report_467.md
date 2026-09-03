# Triple matching report: 467

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eleonore_of_Liechtenstein | hasSpouse | Prince_Karl_Borromäus_of_Liechtenstein |
| Prince_Karl_Borromäus_of_Liechtenstein | hasSibling | Franz_Joseph_I |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Eleonore_of_Liechtenstein | type | Person |
| Eleonore_of_Liechtenstein | type | NamedIndividual |
| Eleonore_of_Liechtenstein | label | "Maria Eleonore of Liechtenstein" |
| Eleonore_of_Liechtenstein | altLabel | "Eleonore of Liechtenstein" |
| Eleonore_of_Liechtenstein | altLabel | "Maria Eleonore of Liechtenstein née Oettingen-Oettingen and Oettingen-Spielberg" |
| Franz_Joseph_I | type | Person |
| Franz_Joseph_I | type | NamedIndividual |
| Franz_Joseph_I | label | "Franz Joseph I, Prince of Liechtenstein" |
| Franz_Joseph_I | altLabel | "Franz Joseph I" |
| Prince_Karl_Borromäus_of_Liechtenstein | type | Person |
| Prince_Karl_Borromäus_of_Liechtenstein | type | NamedIndividual |
| Prince_Karl_Borromäus_of_Liechtenstein | label | "Prince Karl Borromäus of Liechtenstein" |
| Prince_Karl_Borromäus_of_Liechtenstein | altLabel | "Karl Borromäus" |
| Prince_Karl_Borromäus_of_Liechtenstein | altLabel | "Prince Karl (Karl Borromäus) Michael Joseph of Liechtenstein" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
