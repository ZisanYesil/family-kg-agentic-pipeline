# Triple matching report: 895

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Patricia_Ann_Davis | hasParent | Nancy_Davis_Reagan |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Nancy_Davis_Reagan | hasDeathPlace | Bel_Air |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Nancy_Davis_Reagan | type | Person |
| Nancy_Davis_Reagan | type | NamedIndividual |
| Nancy_Davis_Reagan | label | "Nancy Reagan" |
| Nancy_Davis_Reagan | altLabel | "Anne Frances Robbins" |
| Nancy_Davis_Reagan | altLabel | "Nancy Davis Reagan" |
| Patricia_Ann_Davis | type | Person |
| Patricia_Ann_Davis | type | NamedIndividual |
| Patricia_Ann_Davis | label | "Patti Davis" |
| Patricia_Ann_Davis | altLabel | "Patricia Ann Davis" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
