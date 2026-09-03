# Triple matching report: 826

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Award_for_Best_Female_Debut | type | Award |
| Maana_Ke_Hum_Yaar_Nahin | hasCreator | Parineeti_Chopra |
| Maana_Ke_Hum_Yaar_Nahin | hasPerformer | Parineeti_Chopra |
| Maana_Ke_Hum_Yaar_Nahin | type | Artifact |
| Maana_Ke_Hum_Yaar_Nahin | type | CreativeWork |
| Parineeti_Chopra | hasAwardReceived | Filmfare_Award_for_Best_Female_Debut |
| Parineeti_Chopra | type | Agent |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Parineeti_Chopra | hasAwardReceived | award_national_film |
| Parineeti_Chopra | type | Person |
| award_national_film | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 10 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.700000 |
| Recall | 1.000000 |
| F1 score | 0.823529 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
