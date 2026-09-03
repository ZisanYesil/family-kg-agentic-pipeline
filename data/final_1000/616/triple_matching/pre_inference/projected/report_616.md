# Triple matching report: 616

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Aansoo_Ban_Gaye_Phool | hasPublicationDate | "1969"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_First_7th_Night | hasPublicationDate | "2009"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Aansoo_Ban_Gaye_Phool | type | Film |
| Aansoo_Ban_Gaye_Phool | type | NamedIndividual |
| Aansoo_Ban_Gaye_Phool | label | "Aansoo Ban Gaye Phool" |
| The_First_7th_Night | type | Film |
| The_First_7th_Night | type | NamedIndividual |
| The_First_7th_Night | label | "The First 7th Night" |

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
