# Triple matching report: 826

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Maana_Ke_Hum_Yaar_Nahin | hasPerformer | Parineeti_Chopra |
| Parineeti_Chopra | hasAwardReceived | Filmfare_Award_for_Best_Female_Debut |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Award_for_Best_Female_Debut | type | Award |
| Filmfare_Award_for_Best_Female_Debut | type | NamedIndividual |
| Filmfare_Award_for_Best_Female_Debut | label | "Filmfare Award" |
| Maana_Ke_Hum_Yaar_Nahin | type | CreativeWork |
| Maana_Ke_Hum_Yaar_Nahin | type | NamedIndividual |
| Maana_Ke_Hum_Yaar_Nahin | label | "Maana Ke Hum Yaar Nahin" |
| Parineeti_Chopra | hasAwardReceived | award_national_film |
| Parineeti_Chopra | type | Person |
| Parineeti_Chopra | type | NamedIndividual |
| Parineeti_Chopra | label | "Parineeti Chopra" |
| award_national_film | type | Award |
| award_national_film | type | NamedIndividual |
| award_national_film | label | "National Film Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
