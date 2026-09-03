# Triple matching report: 277

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| William_Prince_of_Hohenzollern | hasDeathPlace | Sigmaringen |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Frederick_Prince_of_Hohenzollern | hasParent | William_Prince_of_Hohenzollern |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Frederick_Prince_of_Hohenzollern | type | Person |
| Frederick_Prince_of_Hohenzollern | type | NamedIndividual |
| Frederick_Prince_of_Hohenzollern | label | "Frederick, Prince of Hohenzollern" |
| Sigmaringen | type | Place |
| Sigmaringen | type | NamedIndividual |
| Sigmaringen | label | "Sigmaringen" |
| William_Prince_of_Hohenzollern | hasChild | Frederick_Prince_of_Hohenzollern |
| William_Prince_of_Hohenzollern | type | Person |
| William_Prince_of_Hohenzollern | type | NamedIndividual |
| William_Prince_of_Hohenzollern | label | "William, Prince of Hohenzollern" |

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
