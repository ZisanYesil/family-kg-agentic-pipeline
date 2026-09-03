# Triple matching report: 969

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Phil_Rosen | hasBirthDate | "1888-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Texas_Gun_Fighter | hasDirector | Phil_Rosen |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alice_Guy_Blaché | hasBirthDate | "1873-07-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| What_Will_People_Say | hasDirector | Alice_Guy |

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Phil_Rosen | type | Person |
| Phil_Rosen | type | NamedIndividual |
| Phil_Rosen | label | "Phil Rosen" |
| Phil_Rosen | altLabel | "Philip E. Rosen" |
| Texas_Gun_Fighter | type | Film |
| Texas_Gun_Fighter | type | NamedIndividual |
| Texas_Gun_Fighter | label | "Texas Gun Fighter" |
| What_Will_People_Say | hasDirector | alice_guy |
| What_Will_People_Say | type | Film |
| What_Will_People_Say | type | NamedIndividual |
| What_Will_People_Say | label | "What Will People Say?" |
| alice_guy | hasBirthDate | "1873-07-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| alice_guy | type | Person |
| alice_guy | type | NamedIndividual |
| alice_guy | label | "Alice Guy" |
| alice_guy | altLabel | "Alice Guy‑Blaché" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.111111 |
| Recall | 0.500000 |
| F1 score | 0.181818 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
