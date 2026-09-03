# Triple matching report: 449

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Thomas_Henty | hasParent | Tommy_Cooper |
| Tommy_Cooper | hasCauseOfDeath | heart_attack |

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
| Thomas_Henty | type | Person |
| Thomas_Henty | type | NamedIndividual |
| Thomas_Henty | label | "Thomas Henty" |
| Tommy_Cooper | type | Person |
| Tommy_Cooper | type | NamedIndividual |
| Tommy_Cooper | label | "Tommy Cooper" |
| Tommy_Cooper | altLabel | "Thomas Frederick Cooper" |
| heart_attack | type | CauseOfDeath |
| heart_attack | type | NamedIndividual |
| heart_attack | label | "heart attack" |

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
