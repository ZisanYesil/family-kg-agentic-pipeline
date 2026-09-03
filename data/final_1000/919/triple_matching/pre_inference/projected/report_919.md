# Triple matching report: 919

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Dhammika_Siriwardana | hasDeathDate | "2015-12-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Suwanda_Denuna_Jeewithe | hasDirector | Dhammika_Siriwardana |
| Tjitra | hasDirector | Usmar_Ismail |
| Usmar_Ismail | hasDeathDate | "1971-01-02"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Dhammika_Siriwardana | type | Person |
| Dhammika_Siriwardana | type | NamedIndividual |
| Dhammika_Siriwardana | label | "Dhammika Siriwardana" |
| Suwanda_Denuna_Jeewithe | type | Film |
| Suwanda_Denuna_Jeewithe | type | NamedIndividual |
| Suwanda_Denuna_Jeewithe | label | "Suwanda Denuna Jeewithe" |
| Tjitra | type | Film |
| Tjitra | type | NamedIndividual |
| Tjitra | label | "Tjitra" |
| Usmar_Ismail | type | Person |
| Usmar_Ismail | type | NamedIndividual |
| Usmar_Ismail | label | "Usmar Ismail" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
