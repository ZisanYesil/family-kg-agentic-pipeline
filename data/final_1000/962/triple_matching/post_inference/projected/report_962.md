# Triple matching report: 962

# 1. Matched triples

**Count: 18**

| Subject | Predicate | Object |
|---|---|---|
| British | type | Country |
| British | type | Place |
| Don_Sharp | hasCountry | British |
| Don_Sharp | type | Agent |
| Don_Sharp | type | Person |
| Hennessy_film | hasCreator | Don_Sharp |
| Hennessy_film | hasDirector | Don_Sharp |
| Hennessy_film | type | Artifact |
| Hennessy_film | type | CreativeWork |
| Hennessy_film | type | Film |
| Herbert_Wilcox | hasCountry | British |
| Herbert_Wilcox | type | Agent |
| Herbert_Wilcox | type | Person |
| Trouble_in_the_Glen | hasCreator | Herbert_Wilcox |
| Trouble_in_the_Glen | hasDirector | Herbert_Wilcox |
| Trouble_in_the_Glen | type | Artifact |
| Trouble_in_the_Glen | type | CreativeWork |
| Trouble_in_the_Glen | type | Film |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Australian | type | Country |
| Australian | type | Place |
| Don_Sharp | hasCountry | Australian |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 21 |
| Union triples in scope | 21 |
| True positives (matched) | 18 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 3 |
| Precision | 1.000000 |
| Recall | 0.857143 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
