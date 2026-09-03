# Triple matching report: 84

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| British | type | Country |
| British | type | Place |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Agents_of_Good_Roots | hasCountry | American |
| Agents_of_Good_Roots | type | Artifact |
| The_Human_League | hasCountry | British |
| The_Human_League | type | Artifact |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| agents_of_good_roots | hasCountry | American |
| agents_of_good_roots | type | Agent |
| agents_of_good_roots | type | Organization |
| the_human_league | hasCountry | British |
| the_human_league | type | Agent |
| the_human_league | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 14 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.400000 |
| Recall | 0.500000 |
| F1 score | 0.444444 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
