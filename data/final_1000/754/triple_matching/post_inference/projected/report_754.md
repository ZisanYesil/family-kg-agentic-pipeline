# Triple matching report: 754

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Bunty_Aur_Babli | hasCreator | Shaad_Ali |
| Bunty_Aur_Babli | hasDirector | Shaad_Ali |
| Bunty_Aur_Babli | type | Artifact |
| Bunty_Aur_Babli | type | CreativeWork |
| Bunty_Aur_Babli | type | Film |
| Lawrence_School_Sanawar | type | Agent |
| Lawrence_School_Sanawar | type | EducationalInstitution |
| Lawrence_School_Sanawar | type | Organization |
| Shaad_Ali | hasEducatedAt | Lawrence_School_Sanawar |
| Shaad_Ali | type | Agent |
| Shaad_Ali | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Shaad_Ali | hasEducatedAt | welham_boys_school_educational_institution |
| welham_boys_school_educational_institution | type | Agent |
| welham_boys_school_educational_institution | type | EducationalInstitution |
| welham_boys_school_educational_institution | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.733333 |
| Recall | 1.000000 |
| F1 score | 0.846154 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
