# Triple matching report: 87

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mad_Dogs_and_Englishmen_film | hasCountry | British |
| The_Bond_Boy | hasCountry | American |

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
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "British" |
| Mad_Dogs_and_Englishmen_film | type | Film |
| Mad_Dogs_and_Englishmen_film | type | NamedIndividual |
| Mad_Dogs_and_Englishmen_film | label | "Mad Dogs and Englishmen" |
| The_Bond_Boy | type | Film |
| The_Bond_Boy | type | NamedIndividual |
| The_Bond_Boy | label | "The Bond Boy" |

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
