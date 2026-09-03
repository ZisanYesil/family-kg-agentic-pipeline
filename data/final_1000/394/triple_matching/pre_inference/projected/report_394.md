# Triple matching report: 394

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alice_Gerstenberg | hasCountry | American |
| Nastia_Liukin | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Alice_Gerstenberg | type | Person |
| Alice_Gerstenberg | type | NamedIndividual |
| Alice_Gerstenberg | label | "Alice Gerstenberg" |
| Alice_Gerstenberg | altLabel | "Alice Gerstenberg" |
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| American | altLabel | "United States" |
| Nastia_Liukin | type | Person |
| Nastia_Liukin | type | NamedIndividual |
| Nastia_Liukin | label | "Nastia Liukin" |
| Nastia_Liukin | altLabel | "Nastia Liukin" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
