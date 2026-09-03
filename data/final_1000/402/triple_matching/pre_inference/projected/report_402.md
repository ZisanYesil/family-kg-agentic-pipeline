# Triple matching report: 402

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Basilica_of_St_Lucia_Timotes | hasCountry | Venezuela |
| Saint_Augustine_by_the_Sea_Catholic_Church | hasCountry | United_States |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Basilica_of_St_Lucia_Timotes | type | Artifact |
| Basilica_of_St_Lucia_Timotes | type | NamedIndividual |
| Basilica_of_St_Lucia_Timotes | label | "Basilica of St. Lucia, Timotes" |
| Saint_Augustine_by_the_Sea_Catholic_Church | type | Artifact |
| Saint_Augustine_by_the_Sea_Catholic_Church | type | NamedIndividual |
| Saint_Augustine_by_the_Sea_Catholic_Church | label | "Saint Augustine by the Sea Catholic Church" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |
| United_States | altLabel | "United States" |
| Venezuela | type | Country |
| Venezuela | type | NamedIndividual |
| Venezuela | label | "Venezuela" |
| Venezuela | altLabel | "Venezuela" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
