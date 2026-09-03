# Triple matching report: 55

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Lorentz_Creutz | hasDeathPlace | Öland |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Carl_Gustaf_Creutz | hasParent | Lorentz_Creutz |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Carl_Gustaf_Creutz | type | Person |
| Carl_Gustaf_Creutz | type | NamedIndividual |
| Carl_Gustaf_Creutz | label | "Carl Gustaf Creutz" |
| Lorentz_Creutz | hasParent | Carl_Gustaf_Creutz |
| Lorentz_Creutz | type | Person |
| Lorentz_Creutz | type | NamedIndividual |
| Lorentz_Creutz | label | "Lorentz Creutz Sr." |
| Lorentz_Creutz | altLabel | "Lorentz Creutz" |
| Öland | type | Place |
| Öland | type | NamedIndividual |
| Öland | label | "Battle of Öland" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
