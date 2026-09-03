# Triple matching report: 280

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| I_Will_I_Will_for_Now | hasDirector | Norman_Panama |
| Norman_Panama | hasCauseOfDeath | Parkinson |

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
| I_Will_I_Will_for_Now | type | Film |
| I_Will_I_Will_for_Now | type | NamedIndividual |
| I_Will_I_Will_for_Now | label | "I Will, I Will... for Now" |
| Norman_Panama | type | Person |
| Norman_Panama | type | NamedIndividual |
| Norman_Panama | label | "Norman Panama" |
| Norman_Panama | altLabel | "Norman Kaye Panama" |
| Parkinson | type | CauseOfDeath |
| Parkinson | type | NamedIndividual |
| Parkinson | label | "complications of Parkinson's disease" |

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
