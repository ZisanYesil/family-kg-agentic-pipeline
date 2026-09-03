# Triple matching report: 113

# 1. Matched triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| A_Rough_Passage | hasCreator | Franklyn_Barrett |
| A_Rough_Passage | hasDirector | Franklyn_Barrett |
| A_Rough_Passage | type | Artifact |
| A_Rough_Passage | type | CreativeWork |
| A_Rough_Passage | type | Film |
| Australian | type | Country |
| Australian | type | Place |
| Franklyn_Barrett | hasCountry | Australian |
| Franklyn_Barrett | type | Agent |
| Franklyn_Barrett | type | Person |
| Paul_Scardon | type | Agent |
| Paul_Scardon | type | Person |
| The_Green_God_film | hasCreator | Paul_Scardon |
| The_Green_God_film | hasDirector | Paul_Scardon |
| The_Green_God_film | type | Artifact |
| The_Green_God_film | type | CreativeWork |
| The_Green_God_film | type | Film |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Paul_Scardon | hasCountry | Australian |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 18 |
| True positives (matched) | 17 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 1 |
| Precision | 1.000000 |
| Recall | 0.944444 |
| F1 score | 0.971429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
