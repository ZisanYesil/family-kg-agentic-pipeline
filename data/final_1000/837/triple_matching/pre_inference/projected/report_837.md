# Triple matching report: 837

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Nicht_nachmachen | hasPresenter | Wigald_Boning |
| Wigald_Boning | hasBirthPlace | Wildeshausen |

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
| Nicht_nachmachen | type | CreativeWork |
| Nicht_nachmachen | type | NamedIndividual |
| Nicht_nachmachen | label | "Nicht nachmachen!" |
| Nicht_nachmachen | altLabel | "Don't Imitate!" |
| Wigald_Boning | type | Person |
| Wigald_Boning | type | NamedIndividual |
| Wigald_Boning | label | "Wigald Boning" |
| Wildeshausen | type | Place |
| Wildeshausen | type | NamedIndividual |
| Wildeshausen | label | "Wildeshausen" |

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
