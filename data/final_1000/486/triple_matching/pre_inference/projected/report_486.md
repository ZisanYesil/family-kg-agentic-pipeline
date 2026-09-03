# Triple matching report: 486

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bianca_Riario | hasParent | Caterina_Sforza |
| Caterina_Sforza | hasParent | Galeazzo_Maria_Sforza |

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
| Bianca_Riario | type | Person |
| Bianca_Riario | type | NamedIndividual |
| Bianca_Riario | label | "Bianca Riario" |
| Caterina_Sforza | type | Person |
| Caterina_Sforza | type | NamedIndividual |
| Caterina_Sforza | label | "Caterina Sforza" |
| Galeazzo_Maria_Sforza | type | Person |
| Galeazzo_Maria_Sforza | type | NamedIndividual |
| Galeazzo_Maria_Sforza | label | "Galeazzo Maria Sforza" |

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
