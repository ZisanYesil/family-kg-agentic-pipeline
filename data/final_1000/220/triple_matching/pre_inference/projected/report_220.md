# Triple matching report: 220

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Charlotte_Finch | hasParent | Thomas_Fermor |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Thomas_Fermor_1st_Earl_of_Pomfret | hasParent | Lady_Sophia_Osborne |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Charlotte_Finch | type | Person |
| Lady_Charlotte_Finch | type | NamedIndividual |
| Lady_Charlotte_Finch | label | "Lady Charlotte Finch" |
| Lady_Charlotte_Finch | altLabel | "Charlotte Finch" |
| Lady_Charlotte_Finch | altLabel | "née Fermor" |
| Lady_Sophia_Osborne | type | Person |
| Lady_Sophia_Osborne | type | NamedIndividual |
| Lady_Sophia_Osborne | label | "Lady Sophia Osborne" |
| Lady_Sophia_Osborne | altLabel | "Sophia Osborne" |
| Thomas_Fermor | hasParent | Lady_Sophia_Osborne |
| Thomas_Fermor | type | Person |
| Thomas_Fermor | type | NamedIndividual |
| Thomas_Fermor | label | "Thomas Fermor, 1st Earl of Pomfret" |
| Thomas_Fermor | altLabel | "Thomas Fermor" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
