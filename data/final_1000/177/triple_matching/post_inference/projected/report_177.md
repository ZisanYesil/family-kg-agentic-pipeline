# Triple matching report: 177

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Gillies_MacKinnon | hasEducatedAt | National_Film_and_Television_School |
| Gillies_MacKinnon | type | Agent |
| Gillies_MacKinnon | type | Person |
| National_Film_and_Television_School | type | Agent |
| National_Film_and_Television_School | type | EducationalInstitution |
| National_Film_and_Television_School | type | Organization |
| The_Escapist | hasCreator | Gillies_MacKinnon |
| The_Escapist | hasDirector | Gillies_MacKinnon |
| The_Escapist | type | Artifact |
| The_Escapist | type | CreativeWork |
| The_Escapist | type | Film |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Gillies_MacKinnon | hasEducatedAt | edu_glasgow_school_of_art |
| Gillies_MacKinnon | hasEducatedAt | edu_middlesex_polytechnic |
| edu_glasgow_school_of_art | type | Agent |
| edu_glasgow_school_of_art | type | EducationalInstitution |
| edu_glasgow_school_of_art | type | Organization |
| edu_middlesex_polytechnic | type | Agent |
| edu_middlesex_polytechnic | type | EducationalInstitution |
| edu_middlesex_polytechnic | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 19 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.578947 |
| Recall | 1.000000 |
| F1 score | 0.733333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
