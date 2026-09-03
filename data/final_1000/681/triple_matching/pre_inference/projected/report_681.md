# Triple matching report: 681

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Haribo | hasFounder | Hans_Riegel |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Fraise_Tagada | hasManufacturer | Haribo |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Fraise_Tagada | type | Product |
| Fraise_Tagada | type | NamedIndividual |
| Fraise_Tagada | label | "Fraise Tagada" |
| Hans_Riegel | type | Person |
| Hans_Riegel | type | NamedIndividual |
| Hans_Riegel | label | "Johannes \"Hans\" Riegel, Sr." |
| Haribo | type | Organization |
| Haribo | type | NamedIndividual |
| Haribo | label | "Haribo" |
| Haribo | altLabel | "Haribo Company" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
