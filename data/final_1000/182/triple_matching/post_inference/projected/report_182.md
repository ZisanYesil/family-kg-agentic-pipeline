# Triple matching report: 182

# 1. Matched triples

**Count: 20**

| Subject | Predicate | Object |
|---|---|---|
| A_Heart_in_Winter | hasCreator | Claude_Sautet |
| A_Heart_in_Winter | hasDirector | Claude_Sautet |
| A_Heart_in_Winter | type | Artifact |
| A_Heart_in_Winter | type | CreativeWork |
| A_Heart_in_Winter | type | Film |
| Barbet_Schroeder | hasCountry | Swiss |
| Barbet_Schroeder | type | Agent |
| Barbet_Schroeder | type | Person |
| Claude_Sautet | hasCountry | French |
| Claude_Sautet | type | Agent |
| Claude_Sautet | type | Person |
| French | type | Country |
| French | type | Place |
| Single_White_Female | hasCreator | Barbet_Schroeder |
| Single_White_Female | hasDirector | Barbet_Schroeder |
| Single_White_Female | type | Artifact |
| Single_White_Female | type | CreativeWork |
| Single_White_Female | type | Film |
| Swiss | type | Country |
| Swiss | type | Place |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Barbet_Schroeder | hasCountry | French |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 21 |
| Union triples in scope | 21 |
| True positives (matched) | 20 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 1 |
| Precision | 1.000000 |
| Recall | 0.952381 |
| F1 score | 0.975610 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
