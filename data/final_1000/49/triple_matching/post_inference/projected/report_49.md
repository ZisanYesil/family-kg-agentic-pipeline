# Triple matching report: 49

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Count_Your_Blessings | hasComposer | Franz_Waxman |
| Count_Your_Blessings | hasCreator | Franz_Waxman |
| Count_Your_Blessings | type | Artifact |
| Count_Your_Blessings | type | CreativeWork |
| Franz_Waxman | hasCountry | German |
| Franz_Waxman | type | Agent |
| Franz_Waxman | type | Person |
| German | type | Country |
| German | type | Place |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Count_Your_Blessings | type | Film |
| Franz_Waxman | hasCountry | united_states |
| united_states | type | Country |
| united_states | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.692308 |
| Recall | 1.000000 |
| F1 score | 0.818182 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
