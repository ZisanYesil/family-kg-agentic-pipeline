# Triple matching report: 601

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Japan_Coast_Guard_Museum_Yokohama | hasInception | "2004-12-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| Tain_District_Museum | hasInception | "1966"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Japan_Coast_Guard_Museum_Yokohama | type | Organization |
| Japan_Coast_Guard_Museum_Yokohama | type | NamedIndividual |
| Japan_Coast_Guard_Museum_Yokohama | label | "Japan Coast Guard Museum Yokohama" |
| Tain_District_Museum | type | Organization |
| Tain_District_Museum | type | NamedIndividual |
| Tain_District_Museum | label | "Tain & District Museum" |

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
