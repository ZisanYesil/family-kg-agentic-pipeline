# Triple matching report: 172

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Inthaphom | hasParent | Inthasom |
| Inthasom | hasSibling | Kingkitsarat |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Inthaphom | hasDeathDate | "1776"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Inthaphom | type | Person |
| Inthaphom | type | NamedIndividual |
| Inthaphom | label | "Inthaphom" |
| Inthaphom | altLabel | "Chao Inthaphom" |
| Inthasom | hasDeathDate | "1749"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Inthasom | type | Person |
| Inthasom | type | NamedIndividual |
| Inthasom | label | "Inthasom" |
| Inthasom | altLabel | "Chao Inthasom" |
| Kingkitsarat | type | Person |
| Kingkitsarat | type | NamedIndividual |
| Kingkitsarat | label | "Kingkitsarat" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
