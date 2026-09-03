# Triple matching report: 595

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gordon_Elliott | hasCountry | Australian |
| Road_Tasted | hasCreator | Gordon_Elliott |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Australian | type | Country |
| Australian | type | NamedIndividual |
| Australian | label | "Australia" |
| Australian | altLabel | "Australian" |
| Gordon_Elliott | hasCountry | united_kingdom |
| Gordon_Elliott | type | Person |
| Gordon_Elliott | type | NamedIndividual |
| Gordon_Elliott | label | "Gordon Elliott" |
| Road_Tasted | type | CreativeWork |
| Road_Tasted | type | NamedIndividual |
| Road_Tasted | label | "Road Tasted" |
| united_kingdom | type | Country |
| united_kingdom | type | NamedIndividual |
| united_kingdom | label | "United Kingdom" |
| united_kingdom | altLabel | "British" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.117647 |
| Recall | 1.000000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
