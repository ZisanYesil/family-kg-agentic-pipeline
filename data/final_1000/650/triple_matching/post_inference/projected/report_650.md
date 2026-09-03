# Triple matching report: 650

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Gloria_Macapagal_Arroyo | hasChild | Mikey_Arroyo |
| Gloria_Macapagal_Arroyo | type | Agent |
| Gloria_Macapagal_Arroyo | type | Person |
| Mikey_Arroyo | hasParent | Gloria_Macapagal_Arroyo |
| Mikey_Arroyo | type | Agent |
| Mikey_Arroyo | type | Person |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Ateneo | type | Agent |
| Ateneo | type | Organization |
| Maria_Gloria_Macaraeg_Macapagal_Arroyo | hasEmployer | Ateneo |
| Maria_Gloria_Macaraeg_Macapagal_Arroyo | type | Agent |
| Maria_Gloria_Macaraeg_Macapagal_Arroyo | type | Person |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gloria_Macapagal_Arroyo | hasEmployer | ateneo_de_manila_university |
| ateneo_de_manila_university | type | Agent |
| ateneo_de_manila_university | type | EducationalInstitution |
| ateneo_de_manila_university | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 5 |
| Precision | 0.600000 |
| Recall | 0.545455 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
