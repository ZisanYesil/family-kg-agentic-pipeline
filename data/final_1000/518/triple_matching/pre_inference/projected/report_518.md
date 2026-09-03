# Triple matching report: 518

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Buchanan_Rides_Alone | hasCountry | American |
| The_Good_Old_Naughty_Days | hasCountry | French |

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
| Buchanan_Rides_Alone | type | Artifact |
| Buchanan_Rides_Alone | type | NamedIndividual |
| Buchanan_Rides_Alone | label | "Buchanan Rides Alone" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| The_Good_Old_Naughty_Days | type | Artifact |
| The_Good_Old_Naughty_Days | type | NamedIndividual |
| The_Good_Old_Naughty_Days | label | "The Good Old Naughty Days" |

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
