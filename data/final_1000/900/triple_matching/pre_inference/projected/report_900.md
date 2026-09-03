# Triple matching report: 900

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Manuel_Antonio | hasBirthDate | "1900-07-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| Wilfred_MacDonald | hasBirthDate | "1917-05-02"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Manuel_Antonio | type | Person |
| Manuel_Antonio | type | NamedIndividual |
| Manuel_Antonio | label | "Manuel Antonio" |
| Wilfred_MacDonald | type | Person |
| Wilfred_MacDonald | type | NamedIndividual |
| Wilfred_MacDonald | label | "Wilfred MacDonald" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
