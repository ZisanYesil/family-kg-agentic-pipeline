# Triple matching report: 717

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Adventure_Cycling_Association | hasCountry | U_S |
| Adventure_Cyclist_is_an_association_magazine | hasPublisher | Adventure_Cycling_Association |

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
| Adventure_Cycling_Association | type | Organization |
| Adventure_Cycling_Association | type | NamedIndividual |
| Adventure_Cycling_Association | label | "Adventure Cycling Association" |
| Adventure_Cyclist_is_an_association_magazine | type | CreativeWork |
| Adventure_Cyclist_is_an_association_magazine | type | NamedIndividual |
| Adventure_Cyclist_is_an_association_magazine | label | "Adventure Cyclist magazine" |
| U_S | type | Country |
| U_S | type | NamedIndividual |
| U_S | label | "United States" |

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
