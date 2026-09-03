# Triple matching report: 422

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Ab_Dilli_Dur_Nahin | hasProducer | Raj_Kapoor |
| Ab_Dilli_Dur_Nahin | type | Artifact |
| Ab_Dilli_Dur_Nahin | type | CreativeWork |
| Akkineni_Nagarjuna | hasBirthDate | "1959-08-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Akkineni_Nagarjuna | type | Agent |
| Akkineni_Nagarjuna | type | Person |
| Raj_Kapoor | hasBirthDate | "1924-12-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Raj_Kapoor | type | Agent |
| Raj_Kapoor | type | Person |
| Rarandoi_Veduka_Chudham | type | Artifact |
| Rarandoi_Veduka_Chudham | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Nagarjuna_Akkineni | type | Agent |
| Rarandoi_Veduka_Chudham | hasProducer | Nagarjuna_Akkineni |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Ab_Dilli_Dur_Nahin | type | Film |
| Rarandoi_Veduka_Chudham | hasProducer | Akkineni_Nagarjuna |
| Rarandoi_Veduka_Chudham | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 13 |
| Union triples in scope | 16 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.785714 |
| Recall | 0.846154 |
| F1 score | 0.814815 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
