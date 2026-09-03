# Triple matching report: 962

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Don_Sharp | hasCountry | British |
| Hennessy_film | hasDirector | Don_Sharp |
| Herbert_Wilcox | hasCountry | British |
| Trouble_in_the_Glen | hasDirector | Herbert_Wilcox |

# 2. Unmatched triples

**Total unmatched count: 19**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Don_Sharp | hasCountry | Australian |

## 2.2 Extracted-only triples

**Count: 18**

| Subject | Predicate | Object |
|---|---|---|
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "British" |
| Don_Sharp | type | Person |
| Don_Sharp | type | NamedIndividual |
| Don_Sharp | label | "Don Sharp" |
| Don_Sharp | altLabel | "Donald Herman Sharp" |
| Hennessy_film | type | Film |
| Hennessy_film | type | NamedIndividual |
| Hennessy_film | label | "Hennessy" |
| Herbert_Wilcox | type | Person |
| Herbert_Wilcox | type | NamedIndividual |
| Herbert_Wilcox | label | "Herbert Wilcox" |
| Herbert_Wilcox | altLabel | "Herbert Sydney Wilcox" |
| Trouble_in_the_Glen | type | Film |
| Trouble_in_the_Glen | type | NamedIndividual |
| Trouble_in_the_Glen | label | "Trouble in the Glen" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 22 |
| Ground-truth triples in scope | 5 |
| Union triples in scope | 23 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 18 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.181818 |
| Recall | 0.800000 |
| F1 score | 0.296296 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
