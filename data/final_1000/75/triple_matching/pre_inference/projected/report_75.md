# Triple matching report: 75

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alfonso_II_of_Aragon | hasParent | Ramon_Berenguer_IV |
| Sancha_of_Castile_Queen_of_Aragon | hasSpouse | Alfonso_II_of_Aragon |

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
| Alfonso_II_of_Aragon | type | Person |
| Alfonso_II_of_Aragon | type | NamedIndividual |
| Alfonso_II_of_Aragon | label | "Alfonso II of Aragon" |
| Alfonso_II_of_Aragon | altLabel | "Alfonso II" |
| Ramon_Berenguer_IV | type | Person |
| Ramon_Berenguer_IV | type | NamedIndividual |
| Ramon_Berenguer_IV | label | "Ramon Berenguer IV of Barcelona" |
| Ramon_Berenguer_IV | altLabel | "Count Ramon Berenguer IV of Barcelona" |
| Sancha_of_Castile_Queen_of_Aragon | type | Person |
| Sancha_of_Castile_Queen_of_Aragon | type | NamedIndividual |
| Sancha_of_Castile_Queen_of_Aragon | label | "Sancha of Castile, Queen of Aragon" |
| Sancha_of_Castile_Queen_of_Aragon | altLabel | "Sancha of Castile" |

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
