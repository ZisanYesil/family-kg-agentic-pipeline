# Triple matching report: 507

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Dawn_Fraser | hasOccupation | politician |
| Dawn_Fraser | hasOccupation | swimmer |
| Dunois_Master | hasOccupation | manuscript_illuminator |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Dawn_Fraser | hasBirthDate | "1937-09-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Dawn_Fraser | type | Person |
| Dawn_Fraser | type | NamedIndividual |
| Dawn_Fraser | label | "Dawn Fraser" |
| Dunois_Master | type | Person |
| Dunois_Master | type | NamedIndividual |
| Dunois_Master | label | "Dunois Master" |
| manuscript_illuminator | type | Occupation |
| manuscript_illuminator | type | NamedIndividual |
| manuscript_illuminator | label | "manuscript illuminator" |
| politician | type | Occupation |
| politician | type | NamedIndividual |
| politician | label | "politician" |
| swimmer | type | Occupation |
| swimmer | type | NamedIndividual |
| swimmer | label | "swimmer" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 19 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.157895 |
| Recall | 1.000000 |
| F1 score | 0.272727 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
