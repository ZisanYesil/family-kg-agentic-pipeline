# Triple matching report: 939

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| A_Lego_Brickumentary | hasCountry | American |
| A_Lego_Brickumentary | hasCountry | Danish |
| The_Night_Sitter | hasCountry | American |

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
| A_Lego_Brickumentary | type | Film |
| A_Lego_Brickumentary | type | NamedIndividual |
| A_Lego_Brickumentary | label | "A Lego Brickumentary" |
| A_Lego_Brickumentary | altLabel | "Beyond the Brick: A Lego Brickumentary" |
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Danish | type | Country |
| Danish | type | NamedIndividual |
| Danish | label | "Denmark" |
| Danish | altLabel | "Danish" |
| The_Night_Sitter | type | Film |
| The_Night_Sitter | type | NamedIndividual |
| The_Night_Sitter | label | "The Night Sitter" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 18 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
