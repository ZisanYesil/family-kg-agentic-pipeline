# Triple matching report: 250

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Motu_Hafoka | hasBirthDate | "1987-03-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Motu_Hafoka | hasDeathDate | "2012-06-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Wilhelm_Meise | hasBirthDate | "1901-09-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| Wilhelm_Meise | hasDeathDate | "2002-08-24"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Motu_Hafoka | type | Person |
| Motu_Hafoka | type | NamedIndividual |
| Motu_Hafoka | label | "Motu Hafoka" |
| Wilhelm_Meise | type | Person |
| Wilhelm_Meise | type | NamedIndividual |
| Wilhelm_Meise | label | "Wilhelm Meise" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
