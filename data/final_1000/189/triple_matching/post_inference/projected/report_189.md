# Triple matching report: 189

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Columbus | type | Agent |
| Chris_Columbus | type | Person |
| I_Love_You_Beth_Cooper | hasCreator | Chris_Columbus |
| I_Love_You_Beth_Cooper | hasDirector | Chris_Columbus |
| I_Love_You_Beth_Cooper | type | Artifact |
| I_Love_You_Beth_Cooper | type | CreativeWork |
| I_Love_You_Beth_Cooper | type | Film |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Columbus | hasEducatedAt | Tisch |
| Tisch | type | Agent |
| Tisch | type | EducationalInstitution |
| Tisch | type | Organization |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Columbus | hasEducatedAt | tisch_school_of_the_arts_educational_institution |
| tisch_school_of_the_arts_educational_institution | type | Agent |
| tisch_school_of_the_arts_educational_institution | type | EducationalInstitution |
| tisch_school_of_the_arts_educational_institution | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.636364 |
| Recall | 0.636364 |
| F1 score | 0.636364 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
