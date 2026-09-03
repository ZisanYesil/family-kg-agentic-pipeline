# Triple matching report: 396

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| George_II | hasParent | Princess_Augusta_of_Schwarzburg_Sondershausen |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Princess_Hermine_of_Waldeck_and_Pyrmont | hasParent | George_II |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| George_II | hasChild | Princess_Hermine_of_Waldeck_and_Pyrmont |
| George_II | type | Person |
| George_II | type | NamedIndividual |
| George_II | label | "George II, Prince of Waldeck and Pyrmont" |
| Princess_Augusta_of_Schwarzburg_Sondershausen | type | Person |
| Princess_Augusta_of_Schwarzburg_Sondershausen | type | NamedIndividual |
| Princess_Augusta_of_Schwarzburg_Sondershausen | label | "Countess Princess Augusta of Schwarzburg-Sondershausen" |
| Princess_Hermine_of_Waldeck_and_Pyrmont | type | Person |
| Princess_Hermine_of_Waldeck_and_Pyrmont | type | NamedIndividual |
| Princess_Hermine_of_Waldeck_and_Pyrmont | label | "Princess Hermine of Waldeck and Pyrmont" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
