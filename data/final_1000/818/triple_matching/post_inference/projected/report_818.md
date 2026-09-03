# Triple matching report: 818

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Beautiful_Mexico | hasCreator | Ramón_Pereda |
| Beautiful_Mexico | hasDirector | Ramón_Pereda |
| Beautiful_Mexico | type | Artifact |
| Beautiful_Mexico | type | CreativeWork |
| Beautiful_Mexico | type | Film |
| María_Antonieta_Pons | hasSpouse | Ramón_Pereda |
| María_Antonieta_Pons | type | Agent |
| María_Antonieta_Pons | type | Person |
| Ramón_Pereda | hasSpouse | María_Antonieta_Pons |
| Ramón_Pereda | type | Agent |
| Ramón_Pereda | type | Person |

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
| Ramón_Pereda | hasSpouse | adriana_lamar_person |
| adriana_lamar_person | hasSpouse | Ramón_Pereda |
| adriana_lamar_person | type | Agent |
| adriana_lamar_person | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.733333 |
| Recall | 1.000000 |
| F1 score | 0.846154 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
