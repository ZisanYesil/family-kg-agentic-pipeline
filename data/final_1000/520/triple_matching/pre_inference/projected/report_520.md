# Triple matching report: 520

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| C_Man_film | hasDirector | Joseph_Lerner |
| Greencastle_film | hasDirector | Koran_Dunbar |
| Joseph_Lerner | hasCountry | Canadian |
| Koran_Dunbar | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 19**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 19**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| C_Man_film | type | Film |
| C_Man_film | type | NamedIndividual |
| C_Man_film | label | "C-Man" |
| Canadian | type | Country |
| Canadian | type | NamedIndividual |
| Canadian | label | "Canada" |
| Greencastle_film | type | Film |
| Greencastle_film | type | NamedIndividual |
| Greencastle_film | label | "Greencastle" |
| Joseph_Lerner | type | Person |
| Joseph_Lerner | type | NamedIndividual |
| Joseph_Lerner | label | "Joseph Lerner" |
| Koran_Dunbar | type | Person |
| Koran_Dunbar | type | NamedIndividual |
| Koran_Dunbar | label | "Koran Dunbar" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 23 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 23 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 19 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.173913 |
| Recall | 1.000000 |
| F1 score | 0.296296 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
