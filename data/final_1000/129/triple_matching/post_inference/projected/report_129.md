# Triple matching report: 129

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Bonnie_Tyler | type | Agent |
| Bonnie_Tyler | type | Person |
| I_Believe_in_Your_Sweet_Love | hasCreator | Bonnie_Tyler |
| I_Believe_in_Your_Sweet_Love | hasPerformer | Bonnie_Tyler |
| I_Believe_in_Your_Sweet_Love | type | Artifact |
| I_Believe_in_Your_Sweet_Love | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bonnie_Tyler | hasCountry | United_Kingdom |
| United_Kingdom | type | Country |
| United_Kingdom | type | Place |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bonnie_Tyler | hasCountry | wales |
| wales | type | Country |
| wales | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.666667 |
| Recall | 0.666667 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
