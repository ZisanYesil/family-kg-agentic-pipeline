# Triple matching report: 485

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Korea_Gas_Corporation | hasInception | "1983"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Philips | hasInception | "1891"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Korea_Gas_Corporation | type | Organization |
| Korea_Gas_Corporation | type | NamedIndividual |
| Korea_Gas_Corporation | label | "Korea Gas Corporation" |
| Korea_Gas_Corporation | altLabel | "KOGAS" |
| Korea_Gas_Corporation | altLabel | "Korea Gas Corporation" |
| Philips | type | Organization |
| Philips | type | NamedIndividual |
| Philips | label | "Philips" |
| Philips | altLabel | "Koninklijke Philips N.V." |
| Philips | altLabel | "Philips" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
