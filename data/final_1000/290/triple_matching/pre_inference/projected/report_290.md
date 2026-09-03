# Triple matching report: 290

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Come_Over_to_My_Place | hasPerformer | Davina |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Davina | hasBirthPlace | Detroit |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Come_Over_to_My_Place | type | CreativeWork |
| Come_Over_to_My_Place | type | NamedIndividual |
| Come_Over_to_My_Place | label | "Come Over To My Place" |
| Davina | type | Person |
| Davina | type | NamedIndividual |
| Davina | label | "Davina" |
| Davina | altLabel | "Davina Bussey" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
