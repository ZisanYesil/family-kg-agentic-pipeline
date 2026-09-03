# Triple matching report: 252

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Tannenberg_film | hasCountry | German |
| To_Kill_a_Dragon | hasCountry | German |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| To_Kill_a_Dragon | hasCountry | Soviet |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "Germany" |
| German | altLabel | "German" |
| Tannenberg_film | type | Film |
| Tannenberg_film | type | NamedIndividual |
| Tannenberg_film | label | "Tannenberg" |
| To_Kill_a_Dragon | type | Film |
| To_Kill_a_Dragon | type | NamedIndividual |
| To_Kill_a_Dragon | label | "To Kill a Dragon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.166667 |
| Recall | 0.666667 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
