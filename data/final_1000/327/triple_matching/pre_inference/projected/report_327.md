# Triple matching report: 327

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Folly_to_Be_Wise | hasDirector | Frank_Launder |
| Frank_Launder | hasSpouse | Bernadette_O_Farrell |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Bernadette_O_Farrell | type | Person |
| Bernadette_O_Farrell | type | NamedIndividual |
| Bernadette_O_Farrell | label | "Bernadette O'Farrell" |
| Folly_to_Be_Wise | type | Film |
| Folly_to_Be_Wise | type | NamedIndividual |
| Folly_to_Be_Wise | label | "Folly to Be Wise" |
| Frank_Launder | type | Person |
| Frank_Launder | type | NamedIndividual |
| Frank_Launder | label | "Frank Launder" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
