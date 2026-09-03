# Triple matching report: 177

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gillies_MacKinnon | hasEducatedAt | National_Film_and_Television_School |
| The_Escapist | hasDirector | Gillies_MacKinnon |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Gillies_MacKinnon | hasEducatedAt | edu_glasgow_school_of_art |
| Gillies_MacKinnon | hasEducatedAt | edu_middlesex_polytechnic |
| Gillies_MacKinnon | type | Person |
| Gillies_MacKinnon | type | NamedIndividual |
| Gillies_MacKinnon | label | "Gillies MacKinnon" |
| National_Film_and_Television_School | type | EducationalInstitution |
| National_Film_and_Television_School | type | NamedIndividual |
| National_Film_and_Television_School | label | "National Film and Television School" |
| The_Escapist | type | Film |
| The_Escapist | type | NamedIndividual |
| The_Escapist | label | "The Escapist (2002 film)" |
| edu_glasgow_school_of_art | type | EducationalInstitution |
| edu_glasgow_school_of_art | type | NamedIndividual |
| edu_glasgow_school_of_art | label | "Glasgow School of Art" |
| edu_middlesex_polytechnic | type | EducationalInstitution |
| edu_middlesex_polytechnic | type | NamedIndividual |
| edu_middlesex_polytechnic | label | "Middlesex Polytechnic" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 19 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.105263 |
| Recall | 1.000000 |
| F1 score | 0.190476 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
