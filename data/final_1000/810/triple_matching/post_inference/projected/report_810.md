# Triple matching report: 810

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_Bouvier_Kennedy | type | Agent |
| Caroline_Bouvier_Kennedy | type | Person |
| Jacqueline_Lee_Kennedy_Onassis | hasBirthPlace | Southampton |
| Jacqueline_Lee_Kennedy_Onassis | type | Agent |
| Jacqueline_Lee_Kennedy_Onassis | type | Person |
| Southampton | type | Place |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_Bouvier_Kennedy | hasParent | Jacqueline_Bouvier |
| Jacqueline_Bouvier | hasChild | Caroline_Bouvier_Kennedy |
| Jacqueline_Bouvier | type | Agent |
| Jacqueline_Bouvier | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_Bouvier_Kennedy | hasParent | Jacqueline_Lee_Kennedy_Onassis |
| Jacqueline_Lee_Kennedy_Onassis | hasChild | Caroline_Bouvier_Kennedy |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.750000 |
| Recall | 0.600000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
