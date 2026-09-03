# Triple matching report: 966

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_of_Hesse_Darmstadt | type | Agent |
| Caroline_of_Hesse_Darmstadt | type | Person |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | hasDeathPlace | Pirmasens |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | type | Agent |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | type | Person |
| Pirmasens | type | Place |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_of_Hesse_Darmstadt | hasParent | Louis_IX_Landgrave_of_Hesse_Darmstadt |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | hasChild | Caroline_of_Hesse_Darmstadt |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_of_Hesse_Darmstadt | hasChild | Louis_IX_Landgrave_of_Hesse_Darmstadt |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | hasParent | Caroline_of_Hesse_Darmstadt |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.750000 |
| Recall | 0.750000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
