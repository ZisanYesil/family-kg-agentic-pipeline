# Triple matching report: 140

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Duel_of_Champions | hasCountry | Italian |
| Tarzan_the_Ape_Man_1932_film | hasCountry | American |

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
| Duel_of_Champions | type | Film |
| Duel_of_Champions | type | NamedIndividual |
| Duel_of_Champions | label | "Duel of Champions" |
| Italian | type | Country |
| Italian | type | NamedIndividual |
| Italian | label | "Italy" |
| Italian | altLabel | "Italian" |
| Tarzan_the_Ape_Man_1932_film | type | Film |
| Tarzan_the_Ape_Man_1932_film | type | NamedIndividual |
| Tarzan_the_Ape_Man_1932_film | label | "Tarzan the Ape Man (1932 film)" |

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
