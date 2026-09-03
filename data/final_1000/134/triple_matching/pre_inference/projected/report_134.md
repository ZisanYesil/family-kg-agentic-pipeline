# Triple matching report: 134

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gus_Meins | hasCountry | American |
| Little_Papa | hasDirector | Gus_Meins |

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
| Gus_Meins | hasCountry | germany |
| Gus_Meins | type | Person |
| Gus_Meins | type | NamedIndividual |
| Gus_Meins | label | "Gus Meins" |
| Little_Papa | type | Film |
| Little_Papa | type | NamedIndividual |
| Little_Papa | label | "Little Papa" |
| germany | type | Country |
| germany | type | NamedIndividual |
| germany | label | "Germany" |
| germany | altLabel | "German" |

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
