# Triple matching report: 650

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Mikey_Arroyo | hasParent | Gloria_Macapagal_Arroyo |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Maria_Gloria_Macaraeg_Macapagal_Arroyo | hasEmployer | Ateneo |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Gloria_Macapagal_Arroyo | type | Person |
| Gloria_Macapagal_Arroyo | type | NamedIndividual |
| Gloria_Macapagal_Arroyo | label | "Gloria Macapagal Arroyo" |
| Gloria_Macapagal_Arroyo | altLabel | "Gloria Macapagal-Arroyo" |
| Gloria_Macapagal_Arroyo | altLabel | "Maria Gloria Macaraeg Macapagal-Arroyo" |
| Mikey_Arroyo | type | Person |
| Mikey_Arroyo | type | NamedIndividual |
| Mikey_Arroyo | label | "Mikey Arroyo" |
| Mikey_Arroyo | altLabel | "Juan Miguel Macapagal Arroyo" |
| ateneo_de_manila_university | type | EducationalInstitution |
| ateneo_de_manila_university | type | NamedIndividual |
| ateneo_de_manila_university | label | "Ateneo de Manila University" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
