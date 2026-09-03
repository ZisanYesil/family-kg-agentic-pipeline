# Triple matching report: 632

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Carnic_Alps | hasCountry | Austria |
| Carnic_Alps | hasCountry | Italy |
| Torre_del_Gran_San_Pietro | hasCountry | Italy |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Austria | type | Country |
| Austria | type | NamedIndividual |
| Austria | label | "Austria" |
| Carnic_Alps | type | Place |
| Carnic_Alps | type | NamedIndividual |
| Carnic_Alps | label | "Carnic Alps" |
| Italy | type | Country |
| Italy | type | NamedIndividual |
| Italy | label | "Italy" |
| Torre_del_Gran_San_Pietro | type | Place |
| Torre_del_Gran_San_Pietro | type | NamedIndividual |
| Torre_del_Gran_San_Pietro | label | "Torre del Gran San Pietro" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 15 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
