# Triple matching report: 707

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Elisabeth_of_Bohemia | hasParent | Charles_IV |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charles_IV | hasParent | Elizabeth_of_Bohemia |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Charles_IV | hasParent | elisabeth_of_bohemia_1292 |
| Charles_IV | type | Person |
| Charles_IV | type | NamedIndividual |
| Charles_IV | label | "Charles IV" |
| Charles_IV | altLabel | "Charles IV, Holy Roman Emperor" |
| Elisabeth_of_Bohemia | type | Person |
| Elisabeth_of_Bohemia | type | NamedIndividual |
| Elisabeth_of_Bohemia | label | "Elisabeth of Bohemia" |
| Elisabeth_of_Bohemia | altLabel | "Elisabeth of Bohemia (1358–1373)" |
| elisabeth_of_bohemia_1292 | type | Person |
| elisabeth_of_bohemia_1292 | type | NamedIndividual |
| elisabeth_of_bohemia_1292 | label | "Elisabeth of Bohemia" |
| elisabeth_of_bohemia_1292 | altLabel | "Elisabeth of Bohemia (1292–1330)" |
| elisabeth_of_bohemia_1292 | altLabel | "Elizabeth of Bohemia (1292–1330)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.066667 |
| Recall | 0.500000 |
| F1 score | 0.117647 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
