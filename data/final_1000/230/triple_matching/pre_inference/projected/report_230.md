# Triple matching report: 230

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jim_Henson | hasEducatedAt | University_of_Maryland_College_Park |
| The_Muppets_on_Puppets | hasCreator | Jim_Henson |

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
| Jim_Henson | type | Person |
| Jim_Henson | type | NamedIndividual |
| Jim_Henson | label | "Jim Henson" |
| The_Muppets_on_Puppets | type | CreativeWork |
| The_Muppets_on_Puppets | type | NamedIndividual |
| The_Muppets_on_Puppets | label | "The Muppets on Puppets" |
| University_of_Maryland_College_Park | type | EducationalInstitution |
| University_of_Maryland_College_Park | type | NamedIndividual |
| University_of_Maryland_College_Park | label | "University of Maryland, College Park" |

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
