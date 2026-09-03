# Triple matching report: 345

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Pleasure_1931_film | hasCountry | American |
| Ten_Thousand_Dollars_for_a_Massacre | hasCountry | Italian |

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
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| Italian | type | Country |
| Italian | type | NamedIndividual |
| Italian | label | "Italy" |
| Pleasure_1931_film | type | Film |
| Pleasure_1931_film | type | NamedIndividual |
| Pleasure_1931_film | label | "Pleasure" |
| Ten_Thousand_Dollars_for_a_Massacre | type | Film |
| Ten_Thousand_Dollars_for_a_Massacre | type | NamedIndividual |
| Ten_Thousand_Dollars_for_a_Massacre | label | "Ten Thousand Dollars for a Massacre" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
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
