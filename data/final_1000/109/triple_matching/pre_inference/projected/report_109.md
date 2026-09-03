# Triple matching report: 109

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Christian_Licorice_Store | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Crime_of_Korea | hasCountry | US |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| The_Christian_Licorice_Store | type | Film |
| The_Christian_Licorice_Store | type | NamedIndividual |
| The_Christian_Licorice_Store | label | "The Christian Licorice Store" |
| The_Crime_of_Korea | hasCountry | American |
| The_Crime_of_Korea | type | Film |
| The_Crime_of_Korea | type | NamedIndividual |
| The_Crime_of_Korea | label | "The Crime of Korea" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
