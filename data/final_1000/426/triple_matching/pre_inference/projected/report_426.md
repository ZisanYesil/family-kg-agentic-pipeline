# Triple matching report: 426

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bombshell_The_Hedy_Lamarr_Story | hasCountry | American |
| Toman_film | hasCountry | Czech |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Bombshell_The_Hedy_Lamarr_Story | type | Film |
| Bombshell_The_Hedy_Lamarr_Story | type | NamedIndividual |
| Bombshell_The_Hedy_Lamarr_Story | label | "Bombshell: The Hedy Lamarr Story" |
| Czech | type | Country |
| Czech | type | NamedIndividual |
| Czech | label | "Czech Republic" |
| Czech | altLabel | "Czech" |
| Toman_film | type | Film |
| Toman_film | type | NamedIndividual |
| Toman_film | label | "Toman" |
| Toman_film | altLabel | "Zdeněk Toman" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.117647 |
| Recall | 1.000000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
