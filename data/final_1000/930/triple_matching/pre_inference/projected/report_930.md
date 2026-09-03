# Triple matching report: 930

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Irina_Berezina | hasBirthPlace | Kiev |
| Vladimir_Feldman | hasSpouse | Irina_Berezina |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Irina_Berezina | hasBirthDate | "1965-07-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Irina_Berezina | type | Person |
| Irina_Berezina | type | NamedIndividual |
| Irina_Berezina | label | "Irina Berezina" |
| Irina_Berezina | altLabel | "Irina Berezina-Feldman" |
| Irina_Berezina | altLabel | "Irina Feldman" |
| Kiev | type | Place |
| Kiev | type | NamedIndividual |
| Kiev | label | "Kiev" |
| Vladimir_Feldman | type | Person |
| Vladimir_Feldman | type | NamedIndividual |
| Vladimir_Feldman | label | "Vladimir Feldman" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
