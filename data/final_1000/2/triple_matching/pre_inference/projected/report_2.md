# Triple matching report: 2

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Beat_Girl | hasDirector | Edmond_T_Gréville |
| Edmond_T_Gréville | hasDeathPlace | Nice |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Beat_Girl | type | Film |
| Beat_Girl | type | NamedIndividual |
| Beat_Girl | label | "Beat Girl" |
| Beat_Girl | altLabel | "Beat Girl" |
| Edmond_T_Gréville | type | Person |
| Edmond_T_Gréville | type | NamedIndividual |
| Edmond_T_Gréville | label | "Edmond T. Gréville" |
| Edmond_T_Gréville | altLabel | "Edmond Gréville Thonger" |
| Edmond_T_Gréville | altLabel | "Edmond T. Gréville" |
| Nice | type | Place |
| Nice | type | NamedIndividual |
| Nice | label | "Nice" |
| Nice | altLabel | "Nice" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
