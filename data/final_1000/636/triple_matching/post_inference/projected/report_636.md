# Triple matching report: 636

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Commando_Leopard | hasPublicationDate | "1985"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Commando_Leopard | type | Artifact |
| Commando_Leopard | type | CreativeWork |
| Invasion_of_Astro_Monster | hasPublicationDate | "1965"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Invasion_of_Astro_Monster | type | Artifact |
| Invasion_of_Astro_Monster | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Commando_Leopard | type | Film |
| Invasion_of_Astro_Monster | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
