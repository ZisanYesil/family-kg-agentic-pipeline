# Triple matching report: 152

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Baahubali_2_The_Conclusion | hasProducer | Prasad_Devineni |
| Baahubali_2_The_Conclusion | hasProducer | Shobu_Yarlagadda |
| Baahubali_2_The_Conclusion | type | Artifact |
| Baahubali_2_The_Conclusion | type | CreativeWork |
| Manhattan_Night | type | Artifact |
| Manhattan_Night | type | CreativeWork |
| Prasad_Devineni | type | Agent |
| Shobu_Yarlagadda | type | Agent |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Adrien_Brody | type | Agent |
| Manhattan_Night | hasProducer | Adrien_Brody |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Baahubali_2_The_Conclusion | type | Film |
| Manhattan_Night | type | Film |
| Prasad_Devineni | type | Person |
| Shobu_Yarlagadda | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.666667 |
| Recall | 0.800000 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
