# Triple matching report: 366

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Adolphus_Island | hasCountry | Australia |
| Seal_Island_Victoria | hasCountry | Australia |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Adolphus_Island | type | Place |
| Adolphus_Island | type | NamedIndividual |
| Adolphus_Island | label | "Adolphus Island" |
| Australia | type | Country |
| Australia | type | NamedIndividual |
| Australia | label | "Australia" |
| Seal_Island_Victoria | type | Place |
| Seal_Island_Victoria | type | NamedIndividual |
| Seal_Island_Victoria | label | "Seal Island (Victoria)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
