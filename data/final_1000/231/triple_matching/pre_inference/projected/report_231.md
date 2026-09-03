# Triple matching report: 231

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| John_Williams | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Diamond_Head | hasComposer | John_Williams |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Diamond_Head | type | Film |
| Diamond_Head | type | NamedIndividual |
| Diamond_Head | label | "Diamond Head" |
| John_Williams | type | Person |
| John_Williams | type | NamedIndividual |
| John_Williams | label | "John Williams" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
