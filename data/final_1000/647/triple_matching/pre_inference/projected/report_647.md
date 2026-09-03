# Triple matching report: 647

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| David_Salle | hasEducatedAt | California_Institute_of_the_Arts |
| Search_and_Destroy | hasDirector | David_Salle |

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
| California_Institute_of_the_Arts | type | EducationalInstitution |
| California_Institute_of_the_Arts | type | NamedIndividual |
| California_Institute_of_the_Arts | label | "California Institute of the Arts" |
| David_Salle | type | Person |
| David_Salle | type | NamedIndividual |
| David_Salle | label | "David Salle" |
| Search_and_Destroy | type | Film |
| Search_and_Destroy | type | NamedIndividual |
| Search_and_Destroy | label | "Search and Destroy (1995 film)" |

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
