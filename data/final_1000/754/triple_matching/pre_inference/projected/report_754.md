# Triple matching report: 754

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bunty_Aur_Babli | hasDirector | Shaad_Ali |
| Shaad_Ali | hasEducatedAt | Lawrence_School_Sanawar |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Bunty_Aur_Babli | type | Film |
| Bunty_Aur_Babli | type | NamedIndividual |
| Bunty_Aur_Babli | label | "Bunty Aur Babli" |
| Lawrence_School_Sanawar | type | EducationalInstitution |
| Lawrence_School_Sanawar | type | NamedIndividual |
| Lawrence_School_Sanawar | label | "Lawrence School, Sanawar" |
| Shaad_Ali | hasEducatedAt | welham_boys_school_educational_institution |
| Shaad_Ali | type | Person |
| Shaad_Ali | type | NamedIndividual |
| Shaad_Ali | label | "Shaad Ali" |
| Shaad_Ali | altLabel | "Shaad Ali Sehgal" |
| welham_boys_school_educational_institution | type | EducationalInstitution |
| welham_boys_school_educational_institution | type | NamedIndividual |
| welham_boys_school_educational_institution | label | "Welham Boys' School" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
