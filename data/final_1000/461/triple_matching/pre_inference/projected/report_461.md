# Triple matching report: 461

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Marie_Thérèse_d_Artois | hasParent | Princess_Caroline_of_Naples_and_Sicily |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Marie_Caroline_de_Bourbon_Sicile_duchesse_de_Berry | hasCountry | Italian |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Marie_Thérèse_d_Artois | type | Person |
| Louise_Marie_Thérèse_d_Artois | type | NamedIndividual |
| Louise_Marie_Thérèse_d_Artois | label | "Louise Marie Thérèse d'Artois" |
| Princess_Caroline_of_Naples_and_Sicily | hasCountry | naples_and_sicily |
| Princess_Caroline_of_Naples_and_Sicily | type | Person |
| Princess_Caroline_of_Naples_and_Sicily | type | NamedIndividual |
| Princess_Caroline_of_Naples_and_Sicily | label | "Princess Caroline of Naples and Sicily" |
| naples_and_sicily | type | Country |
| naples_and_sicily | type | NamedIndividual |
| naples_and_sicily | label | "Naples and Sicily" |
| naples_and_sicily | altLabel | "Naples" |
| naples_and_sicily | altLabel | "Sicily" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
