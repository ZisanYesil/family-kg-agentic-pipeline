# Triple matching report: 370

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Franz_Schubert | hasStudentOf | Antonio_Salieri |
| Gretchen_am_Spinnrade | hasComposer | Franz_Schubert |

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
| Antonio_Salieri | type | Person |
| Antonio_Salieri | type | NamedIndividual |
| Antonio_Salieri | label | "Antonio Salieri" |
| Antonio_Salieri | altLabel | "Antonio Salieri" |
| Franz_Schubert | type | Person |
| Franz_Schubert | type | NamedIndividual |
| Franz_Schubert | label | "Franz Schubert" |
| Franz_Schubert | altLabel | "Franz Peter Schubert" |
| Franz_Schubert | altLabel | "Franz Schubert" |
| Gretchen_am_Spinnrade | type | MusicalWork |
| Gretchen_am_Spinnrade | type | NamedIndividual |
| Gretchen_am_Spinnrade | label | "Gretchen am Spinnrade" |
| Gretchen_am_Spinnrade | altLabel | "Gretchen am Spinnrade" |

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
