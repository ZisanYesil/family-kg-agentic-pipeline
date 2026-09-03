# Triple matching report: 896

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Far_Away_and_Long_Ago | hasPublicationDate | "1978"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| I_Always_Loved_You | hasPublicationDate | "1953"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Far_Away_and_Long_Ago | type | Film |
| Far_Away_and_Long_Ago | type | NamedIndividual |
| Far_Away_and_Long_Ago | label | "Far Away and Long Ago" |
| I_Always_Loved_You | type | Film |
| I_Always_Loved_You | type | NamedIndividual |
| I_Always_Loved_You | label | "I Always Loved You" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
