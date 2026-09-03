# Triple matching report: 954

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Jack_Klugman | hasBirthDate | "1922-04-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jack_Klugman | hasDeathDate | "2012-12-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Rembrandt_Bugatti | hasBirthDate | "1884-10-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Rembrandt_Bugatti | hasDeathDate | "1916-01-08"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Jack_Klugman | type | Person |
| Jack_Klugman | type | NamedIndividual |
| Jack_Klugman | label | "Jack Klugman" |
| Rembrandt_Bugatti | type | Person |
| Rembrandt_Bugatti | type | NamedIndividual |
| Rembrandt_Bugatti | label | "Rembrandt Bugatti" |

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
