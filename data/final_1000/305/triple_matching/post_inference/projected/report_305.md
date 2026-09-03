# Triple matching report: 305

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Margaret_Atwood_Once_in_August | hasCreator | Michael_Rubbo |
| Margaret_Atwood_Once_in_August | hasDirector | Michael_Rubbo |
| Margaret_Atwood_Once_in_August | type | Artifact |
| Margaret_Atwood_Once_in_August | type | CreativeWork |
| Margaret_Atwood_Once_in_August | type | Film |
| Michael_Rubbo | type | Agent |
| Michael_Rubbo | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fulbright_Scholarship | type | Award |
| Michael_Rubbo | hasAwardReceived | Fulbright_Scholarship |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 9 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.777778 |
| F1 score | 0.875000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
