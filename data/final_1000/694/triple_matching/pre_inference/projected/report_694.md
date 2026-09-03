# Triple matching report: 694

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chilperic_I | hasParent | Aregund |
| Fredegund | hasSpouse | Chilperic_I |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Aregund | type | Person |
| Aregund | type | NamedIndividual |
| Aregund | label | "Aregund" |
| Aregund | altLabel | "Aregund" |
| Chilperic_I | type | Person |
| Chilperic_I | type | NamedIndividual |
| Chilperic_I | label | "Chilperic I" |
| Chilperic_I | altLabel | "Chilperic I" |
| Fredegund | hasDeathDate | "0597-12-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Fredegund | type | Person |
| Fredegund | type | NamedIndividual |
| Fredegund | label | "Fredegund" |
| Fredegund | altLabel | "Fredegund" |
| Fredegund | altLabel | "Fredegunda" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
