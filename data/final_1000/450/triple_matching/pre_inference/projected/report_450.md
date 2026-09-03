# Triple matching report: 450

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Truth_or_Consequences_N_M | hasDirector | Kiefer_Sutherland |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Kiefer_Sutherland | hasChild | Sarah_Sutherland |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Kiefer_Sutherland | type | Person |
| Kiefer_Sutherland | type | NamedIndividual |
| Kiefer_Sutherland | label | "Kiefer Sutherland" |
| Sarah_Sutherland | hasParent | Kiefer_Sutherland |
| Sarah_Sutherland | type | Person |
| Sarah_Sutherland | type | NamedIndividual |
| Sarah_Sutherland | label | "Sarah Sutherland" |
| Truth_or_Consequences_N_M | type | Film |
| Truth_or_Consequences_N_M | type | NamedIndividual |
| Truth_or_Consequences_N_M | label | "Truth or Consequences, N.M." |

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
