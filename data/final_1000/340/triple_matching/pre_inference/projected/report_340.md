# Triple matching report: 340

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Der_Doppelgänger | hasComposer | Franz_Schubert |
| Franz_Schubert | hasStudentOf | Antonio_Salieri |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Antonio_Salieri | type | Person |
| Antonio_Salieri | type | NamedIndividual |
| Antonio_Salieri | label | "Antonio Salieri" |
| Der_Doppelgänger | type | MusicalWork |
| Der_Doppelgänger | type | NamedIndividual |
| Der_Doppelgänger | label | "Der Doppelgänger" |
| Franz_Schubert | type | Person |
| Franz_Schubert | type | NamedIndividual |
| Franz_Schubert | label | "Franz Schubert" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
