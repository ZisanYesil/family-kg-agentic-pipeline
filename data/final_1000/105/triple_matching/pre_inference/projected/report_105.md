# Triple matching report: 105

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Keeper_of_the_Bees_1935_film | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| God_s_Ears | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| God_s_Ears | type | Film |
| God_s_Ears | type | NamedIndividual |
| God_s_Ears | label | "God's Ears" |
| The_Keeper_of_the_Bees_1935_film | type | Film |
| The_Keeper_of_the_Bees_1935_film | type | NamedIndividual |
| The_Keeper_of_the_Bees_1935_film | label | "The Keeper of the Bees (1935 film)" |

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
