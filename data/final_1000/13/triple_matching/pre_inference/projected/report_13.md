# Triple matching report: 13

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| American_Scientist | hasPublisher | Sigma_Xi |
| Sigma_Xi | hasInception | "1886"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| American_Scientist | type | CreativeWork |
| American_Scientist | type | NamedIndividual |
| American_Scientist | label | "American Scientist" |
| Sigma_Xi | type | Organization |
| Sigma_Xi | type | NamedIndividual |
| Sigma_Xi | label | "Sigma Xi" |
| Sigma_Xi | altLabel | "Sigma Xi, The Scientific Research Society" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
