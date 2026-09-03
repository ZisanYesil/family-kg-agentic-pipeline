# Triple matching report: 195

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Mystery_Plane | hasCountry | American |
| To_Kill_a_Dragon | hasCountry | German |
| To_Kill_a_Dragon | hasCountry | Soviet |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 18**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "Germany" |
| German | altLabel | "German" |
| Mystery_Plane | type | Film |
| Mystery_Plane | type | NamedIndividual |
| Mystery_Plane | label | "Mystery Plane" |
| Soviet | type | Country |
| Soviet | type | NamedIndividual |
| Soviet | label | "Soviet Union" |
| Soviet | altLabel | "Soviet" |
| To_Kill_a_Dragon | type | Film |
| To_Kill_a_Dragon | type | NamedIndividual |
| To_Kill_a_Dragon | label | "To Kill a Dragon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 21 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 21 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 18 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
