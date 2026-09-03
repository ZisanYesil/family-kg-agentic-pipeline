# Triple matching report: 422

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Ab_Dilli_Dur_Nahin | hasProducer | Raj_Kapoor |
| Akkineni_Nagarjuna | hasBirthDate | "1959-08-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Raj_Kapoor | hasBirthDate | "1924-12-14"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Rarandoi_Veduka_Chudham | hasProducer | Nagarjuna_Akkineni |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Ab_Dilli_Dur_Nahin | type | Film |
| Ab_Dilli_Dur_Nahin | type | NamedIndividual |
| Ab_Dilli_Dur_Nahin | label | "Ab Dilli Dur Nahin" |
| Akkineni_Nagarjuna | type | Person |
| Akkineni_Nagarjuna | type | NamedIndividual |
| Akkineni_Nagarjuna | label | "Akkineni Nagarjuna" |
| Raj_Kapoor | type | Person |
| Raj_Kapoor | type | NamedIndividual |
| Raj_Kapoor | label | "Raj Kapoor" |
| Rarandoi_Veduka_Chudham | hasProducer | Akkineni_Nagarjuna |
| Rarandoi_Veduka_Chudham | type | Film |
| Rarandoi_Veduka_Chudham | type | NamedIndividual |
| Rarandoi_Veduka_Chudham | label | "Rarandoi Veduka Chudham" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 17 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.187500 |
| Recall | 0.750000 |
| F1 score | 0.300000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
