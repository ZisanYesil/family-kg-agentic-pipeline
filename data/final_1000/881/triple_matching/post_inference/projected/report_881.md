# Triple matching report: 881

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Auguste_Théodore_Paul_de_Broglie | type | Agent |
| Auguste_Théodore_Paul_de_Broglie | type | Person |
| Victor_de_Broglie | type | Agent |
| Victor_de_Broglie | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Albertine_baroness_Staël_von_Holstein | hasChild | Auguste_Théodore_Paul_de_Broglie |
| Albertine_baroness_Staël_von_Holstein | hasSpouse | Victor_de_Broglie |
| Albertine_baroness_Staël_von_Holstein | type | Agent |
| Albertine_baroness_Staël_von_Holstein | type | Person |
| Auguste_Théodore_Paul_de_Broglie | hasParent | Albertine_baroness_Staël_von_Holstein |
| Victor_de_Broglie | hasSpouse | Albertine_baroness_Staël_von_Holstein |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Auguste_Théodore_Paul_de_Broglie | hasParent | Victor_de_Broglie |
| Victor_de_Broglie | hasChild | Auguste_Théodore_Paul_de_Broglie |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.666667 |
| Recall | 0.400000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
