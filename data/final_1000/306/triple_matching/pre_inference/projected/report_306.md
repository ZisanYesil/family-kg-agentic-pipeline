# Triple matching report: 306

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Rajiv_Gandhi | hasSibling | Sanjay_Gandhi |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Priyanka_Gandhi | hasParent | Rajiv_Gandhi |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Priyanka_Gandhi | type | Person |
| Priyanka_Gandhi | type | NamedIndividual |
| Priyanka_Gandhi | label | "Priyanka Gandhi" |
| Priyanka_Gandhi | altLabel | "Priyanka Gandhi Vadra" |
| Rajiv_Gandhi | hasChild | Priyanka_Gandhi |
| Rajiv_Gandhi | type | Person |
| Rajiv_Gandhi | type | NamedIndividual |
| Rajiv_Gandhi | label | "Rajiv Gandhi" |
| Sanjay_Gandhi | type | Person |
| Sanjay_Gandhi | type | NamedIndividual |
| Sanjay_Gandhi | label | "Sanjay Gandhi" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
