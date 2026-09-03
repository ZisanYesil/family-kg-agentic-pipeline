# Triple matching report: 704

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hero_at_Large | hasDirector | Martin_Davidson |
| Martin_Davidson | hasEducatedAt | American_Academy_of_Dramatic_Arts |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| American_Academy_of_Dramatic_Arts | type | EducationalInstitution |
| American_Academy_of_Dramatic_Arts | type | NamedIndividual |
| American_Academy_of_Dramatic_Arts | label | "American Academy of Dramatic Arts" |
| Hero_at_Large | type | Film |
| Hero_at_Large | type | NamedIndividual |
| Hero_at_Large | label | "Hero At Large" |
| Martin_Davidson | type | Person |
| Martin_Davidson | type | NamedIndividual |
| Martin_Davidson | label | "Martin Davidson" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
