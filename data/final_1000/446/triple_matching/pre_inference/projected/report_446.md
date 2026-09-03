# Triple matching report: 446

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Emilio_Drake_1st_Marquess_of_Cañada_Honda | hasBirthDate | "1855-01-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Emilio_Drake_1st_Marquess_of_Cañada_Honda | hasDeathDate | "1915-07-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Franjo_Marković | hasBirthDate | "1845-07-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Franjo_Marković | hasDeathDate | "1914-09-15"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Emilio_Drake_1st_Marquess_of_Cañada_Honda | type | Person |
| Emilio_Drake_1st_Marquess_of_Cañada_Honda | type | NamedIndividual |
| Emilio_Drake_1st_Marquess_of_Cañada_Honda | label | "Emilio Drake, 1st Marquess of Cañada Honda" |
| Emilio_Drake_1st_Marquess_of_Cañada_Honda | altLabel | "Emilio María Juan Crisostomo Drake y de la Cerda" |
| Franjo_Marković | type | Person |
| Franjo_Marković | type | NamedIndividual |
| Franjo_Marković | label | "Franjo Marković" |
| Franjo_Marković | altLabel | "Franjo Marković" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.333333 |
| Recall | 1.000000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
