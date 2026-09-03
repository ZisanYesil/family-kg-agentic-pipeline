# Triple matching report: 55

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Carl_Gustaf_Creutz | type | Agent |
| Carl_Gustaf_Creutz | type | Person |
| Lorentz_Creutz | hasDeathPlace | Öland |
| Lorentz_Creutz | type | Agent |
| Lorentz_Creutz | type | Person |
| Öland | type | Place |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Carl_Gustaf_Creutz | hasParent | Lorentz_Creutz |
| Lorentz_Creutz | hasChild | Carl_Gustaf_Creutz |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Carl_Gustaf_Creutz | hasChild | Lorentz_Creutz |
| Lorentz_Creutz | hasParent | Carl_Gustaf_Creutz |

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
