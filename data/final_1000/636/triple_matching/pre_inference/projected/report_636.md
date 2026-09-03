# Triple matching report: 636

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Commando_Leopard | hasPublicationDate | "1985"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Invasion_of_Astro_Monster | hasPublicationDate | "1965"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Commando_Leopard | type | Film |
| Commando_Leopard | type | NamedIndividual |
| Commando_Leopard | label | "Commando Leopard" |
| Invasion_of_Astro_Monster | type | Film |
| Invasion_of_Astro_Monster | type | NamedIndividual |
| Invasion_of_Astro_Monster | label | "Invasion of Astro-Monster" |
| Invasion_of_Astro_Monster | altLabel | "Invasion Of Astro-Monster" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
