# Triple matching report: 189

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| I_Love_You_Beth_Cooper | hasDirector | Chris_Columbus |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Columbus | hasEducatedAt | Tisch |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Columbus | hasEducatedAt | tisch_school_of_the_arts_educational_institution |
| Chris_Columbus | type | Person |
| Chris_Columbus | type | NamedIndividual |
| Chris_Columbus | label | "Chris Columbus" |
| Chris_Columbus | altLabel | "Chris Joseph Columbus" |
| I_Love_You_Beth_Cooper | type | Film |
| I_Love_You_Beth_Cooper | type | NamedIndividual |
| I_Love_You_Beth_Cooper | label | "I Love You, Beth Cooper" |
| I_Love_You_Beth_Cooper | altLabel | "I Love You, Beth Cooper (film)" |
| tisch_school_of_the_arts_educational_institution | type | EducationalInstitution |
| tisch_school_of_the_arts_educational_institution | type | NamedIndividual |
| tisch_school_of_the_arts_educational_institution | label | "Tisch School of the Arts" |

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
