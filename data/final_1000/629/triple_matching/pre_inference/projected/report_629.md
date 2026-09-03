# Triple matching report: 629

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alfonso_VII_of_León_and_Castile | hasParent | Urraca_of_León |
| Sancha_of_Castile_Queen_of_Navarre | hasParent | Alfonso_VII_of_León_and_Castile |

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
| Alfonso_VII_of_León_and_Castile | type | Person |
| Alfonso_VII_of_León_and_Castile | type | NamedIndividual |
| Alfonso_VII_of_León_and_Castile | label | "Alfonso VII of León and Castile" |
| Sancha_of_Castile_Queen_of_Navarre | type | Person |
| Sancha_of_Castile_Queen_of_Navarre | type | NamedIndividual |
| Sancha_of_Castile_Queen_of_Navarre | label | "Sancha of Castile" |
| Urraca_of_León | type | Person |
| Urraca_of_León | type | NamedIndividual |
| Urraca_of_León | label | "Urraca of León" |

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
