# Triple matching report: 818

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Beautiful_Mexico | hasDirector | Ramón_Pereda |
| Ramón_Pereda | hasSpouse | María_Antonieta_Pons |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Beautiful_Mexico | type | Film |
| Beautiful_Mexico | type | NamedIndividual |
| Beautiful_Mexico | label | "Beautiful Mexico" |
| María_Antonieta_Pons | type | Person |
| María_Antonieta_Pons | type | NamedIndividual |
| María_Antonieta_Pons | label | "María Antonieta Pons" |
| Ramón_Pereda | hasSpouse | adriana_lamar_person |
| Ramón_Pereda | type | Person |
| Ramón_Pereda | type | NamedIndividual |
| Ramón_Pereda | label | "Ramón Pereda" |
| adriana_lamar_person | type | Person |
| adriana_lamar_person | type | NamedIndividual |
| adriana_lamar_person | label | "Adriana Lamar" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
