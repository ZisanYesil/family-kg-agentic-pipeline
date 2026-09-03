# Triple matching report: 254

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| The_Hideout_film | hasCountry | American |
| The_Hideout_film | hasCountry | Italian |
| Trieste_mia | hasCountry | Italian |

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
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Italian | type | Country |
| Italian | type | NamedIndividual |
| Italian | label | "Italy" |
| Italian | altLabel | "Italian" |
| The_Hideout_film | type | Film |
| The_Hideout_film | type | NamedIndividual |
| The_Hideout_film | label | "The Hideout" |
| Trieste_mia | type | Film |
| Trieste_mia | type | NamedIndividual |
| Trieste_mia | label | "Trieste mia!" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 17 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.176471 |
| Recall | 1.000000 |
| F1 score | 0.300000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
