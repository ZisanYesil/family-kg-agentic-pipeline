# Triple matching report: 955

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Pieter_van_Vollenhoven | hasBirthDate | "1939-04-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Prince_Maurits_of_Orange_Nassau_van_Vollenhoven | hasParent | Pieter_van_Vollenhoven |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Pieter_van_Vollenhoven | type | Person |
| Pieter_van_Vollenhoven | type | NamedIndividual |
| Pieter_van_Vollenhoven | label | "Pieter van Vollenhoven" |
| Pieter_van_Vollenhoven | altLabel | "Pieter van Vollenhoven Jr." |
| Prince_Maurits_of_Orange_Nassau_van_Vollenhoven | type | Person |
| Prince_Maurits_of_Orange_Nassau_van_Vollenhoven | type | NamedIndividual |
| Prince_Maurits_of_Orange_Nassau_van_Vollenhoven | label | "Prince Maurits Willem Pieter Hendrik of Orange-Nassau, van Vollenhoven" |
| Prince_Maurits_of_Orange_Nassau_van_Vollenhoven | altLabel | "Prince Maurits of Orange-Nassau, van Vollenhoven" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
