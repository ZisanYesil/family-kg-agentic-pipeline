# Triple matching report: 755

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Before_the_Streets | hasCountry | Canadian |
| Buchanan_Rides_Alone | hasCountry | American |

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
| Before_the_Streets | type | Film |
| Before_the_Streets | type | NamedIndividual |
| Before_the_Streets | label | "Before the Streets" |
| Buchanan_Rides_Alone | type | Film |
| Buchanan_Rides_Alone | type | NamedIndividual |
| Buchanan_Rides_Alone | label | "Buchanan Rides Alone" |
| Canadian | type | Country |
| Canadian | type | NamedIndividual |
| Canadian | label | "Canada" |
| Canadian | altLabel | "Canadian" |

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
