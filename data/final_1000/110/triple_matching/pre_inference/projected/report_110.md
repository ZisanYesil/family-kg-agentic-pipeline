# Triple matching report: 110

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| 3096_Days | hasDirector | Sherry_Horman |
| Sherry_Horman | hasCountry | American |

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
| 3096_Days | type | Film |
| 3096_Days | type | NamedIndividual |
| 3096_Days | label | "3096 Days" |
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Sherry_Horman | hasCountry | country_germany |
| Sherry_Horman | type | Person |
| Sherry_Horman | type | NamedIndividual |
| Sherry_Horman | label | "Sherry Hormann" |
| country_germany | type | Country |
| country_germany | type | NamedIndividual |
| country_germany | label | "Germany" |
| country_germany | altLabel | "German" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
