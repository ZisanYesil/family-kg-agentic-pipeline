# Triple matching report: 476

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Edouard_Brissaud | hasBirthPlace | Besançon |
| Pierre_Brissaud | hasParent | Edouard_Brissaud |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Besançon | type | Place |
| Besançon | type | NamedIndividual |
| Besançon | label | "Besançon" |
| Edouard_Brissaud | type | Person |
| Edouard_Brissaud | type | NamedIndividual |
| Edouard_Brissaud | label | "Édouard Brissaud" |
| Edouard_Brissaud | altLabel | "Edouard Brissaud" |
| Pierre_Brissaud | type | Person |
| Pierre_Brissaud | type | NamedIndividual |
| Pierre_Brissaud | label | "Pierre Brissaud" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
