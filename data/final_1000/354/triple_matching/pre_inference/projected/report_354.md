# Triple matching report: 354

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Prince | hasCountry | American |
| When_You_Were_Mine | hasComposer | Prince |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Prince | type | Person |
| Prince | type | NamedIndividual |
| Prince | label | "Prince Rogers Nelson" |
| Prince | altLabel | "Prince" |
| When_You_Were_Mine | type | MusicalWork |
| When_You_Were_Mine | type | NamedIndividual |
| When_You_Were_Mine | label | "When You Were Mine" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
