# Triple matching report: 163

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Andy_Warhol | hasCountry | American |
| Beauty_No_1 | hasDirector | Andy_Warhol |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Andy_Warhol | type | Person |
| Andy_Warhol | type | NamedIndividual |
| Andy_Warhol | label | "Andy Warhol" |
| Beauty_No_1 | type | Film |
| Beauty_No_1 | type | NamedIndividual |
| Beauty_No_1 | label | "Beauty No. 1" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
