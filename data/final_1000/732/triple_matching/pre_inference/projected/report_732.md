# Triple matching report: 732

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Diane_Warren | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Cry_Over_Me | hasComposer | Diane_Warren |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Cry_Over_Me | type | CreativeWork |
| Cry_Over_Me | type | NamedIndividual |
| Cry_Over_Me | label | "Cry Over Me" |
| Cry_Over_Me | altLabel | "Cry Over Me" |
| Diane_Warren | type | Person |
| Diane_Warren | type | NamedIndividual |
| Diane_Warren | label | "Diane Warren" |
| Diane_Warren | altLabel | "Diane Warren" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
