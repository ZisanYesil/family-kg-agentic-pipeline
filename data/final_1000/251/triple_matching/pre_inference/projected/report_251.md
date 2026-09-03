# Triple matching report: 251

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alam_Shah | hasParent | Muhammad_Shah |
| Muhammad_Shah | hasBurialPlace | Lodi_Gardens |

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
| Alam_Shah | type | Person |
| Alam_Shah | type | NamedIndividual |
| Alam_Shah | label | "Alam Shah" |
| Lodi_Gardens | type | Place |
| Lodi_Gardens | type | NamedIndividual |
| Lodi_Gardens | label | "Lodi Gardens" |
| Lodi_Gardens | altLabel | "New Delhi" |
| Muhammad_Shah | type | Person |
| Muhammad_Shah | type | NamedIndividual |
| Muhammad_Shah | label | "Muhammad Shah" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
