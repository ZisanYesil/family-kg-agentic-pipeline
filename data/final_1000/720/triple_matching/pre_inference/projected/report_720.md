# Triple matching report: 720

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Douglas_MacArthur | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_MacArthur_IV | hasParent | Douglas_MacArthur |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Arthur_MacArthur_IV | type | Person |
| Arthur_MacArthur_IV | type | NamedIndividual |
| Arthur_MacArthur_IV | label | "Arthur MacArthur IV" |
| Douglas_MacArthur | hasParent | Arthur_MacArthur_IV |
| Douglas_MacArthur | type | Person |
| Douglas_MacArthur | type | NamedIndividual |
| Douglas_MacArthur | label | "Douglas MacArthur" |

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
