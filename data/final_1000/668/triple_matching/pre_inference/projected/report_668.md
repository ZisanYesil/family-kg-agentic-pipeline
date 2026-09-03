# Triple matching report: 668

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Franz_Schubert | hasStudentOf | Antonio_Salieri |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Prometheus | hasComposer | Franz_Schubert |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Antonio_Salieri | type | Person |
| Antonio_Salieri | type | NamedIndividual |
| Antonio_Salieri | label | "Antonio Salieri" |
| Franz_Schubert | type | Person |
| Franz_Schubert | type | NamedIndividual |
| Franz_Schubert | label | "Franz Schubert" |
| Prometheus | type | CreativeWork |
| Prometheus | type | NamedIndividual |
| Prometheus | label | "Prometheus (art song)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
