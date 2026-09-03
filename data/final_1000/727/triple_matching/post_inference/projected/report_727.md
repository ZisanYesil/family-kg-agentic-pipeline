# Triple matching report: 727

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Chantilly_Lace | hasCreator | Linda_Yellen |
| Chantilly_Lace | hasDirector | Linda_Yellen |
| Chantilly_Lace | type | Artifact |
| Chantilly_Lace | type | CreativeWork |
| Chantilly_Lace | type | Film |
| Emmys | type | Award |
| Linda_Yellen | hasAwardReceived | Emmys |
| Linda_Yellen | type | Agent |
| Linda_Yellen | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Linda_Yellen | hasAwardReceived | christopher_award |
| Linda_Yellen | hasAwardReceived | peabody_award |
| Linda_Yellen | hasAwardReceived | primetime_emmy_award |
| Linda_Yellen | hasAwardReceived | silver_nymph_award |
| christopher_award | type | Award |
| peabody_award | type | Award |
| primetime_emmy_award | type | Award |
| silver_nymph_award | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 17 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.529412 |
| Recall | 1.000000 |
| F1 score | 0.692308 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
