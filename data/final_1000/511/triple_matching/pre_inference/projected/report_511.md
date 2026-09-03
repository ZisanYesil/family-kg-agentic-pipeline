# Triple matching report: 511

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Herb_Alpert | hasSpouse | Lani_Hall |
| Mae | hasPerformer | Herb_Alpert |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Herb_Alpert | type | Person |
| Herb_Alpert | type | NamedIndividual |
| Herb_Alpert | label | "Herb Alpert" |
| Herb_Alpert | altLabel | "Herb Alpert" |
| Lani_Hall | type | Person |
| Lani_Hall | type | NamedIndividual |
| Lani_Hall | label | "Lani Hall" |
| Lani_Hall | altLabel | "Lani Hall" |
| Mae | type | CreativeWork |
| Mae | type | NamedIndividual |
| Mae | label | "Mae (Riz Ortolani song)" |
| Mae | altLabel | "Mae" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
