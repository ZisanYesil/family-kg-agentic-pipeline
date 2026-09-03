# Triple matching report: 138

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Heart_of_Stone_1950_film | hasCountry | German |
| The_Plaything_of_Broadway | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "East Germany" |
| German | altLabel | "East German" |
| Heart_of_Stone_1950_film | type | Film |
| Heart_of_Stone_1950_film | type | NamedIndividual |
| Heart_of_Stone_1950_film | label | "Heart of Stone (1950 film)" |
| The_Plaything_of_Broadway | type | Film |
| The_Plaything_of_Broadway | type | NamedIndividual |
| The_Plaything_of_Broadway | label | "The Plaything of Broadway" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
