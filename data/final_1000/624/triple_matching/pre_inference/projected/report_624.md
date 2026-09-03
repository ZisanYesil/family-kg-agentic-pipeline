# Triple matching report: 624

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Sólveig_Anspach | hasEducatedAt | La_Fémis |
| The_Aquatic_Effect | hasDirector | Sólveig_Anspach |

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
| La_Fémis | type | EducationalInstitution |
| La_Fémis | type | NamedIndividual |
| La_Fémis | label | "La Fémis" |
| Sólveig_Anspach | type | Person |
| Sólveig_Anspach | type | NamedIndividual |
| Sólveig_Anspach | label | "Sólveig Anspach" |
| The_Aquatic_Effect | type | Film |
| The_Aquatic_Effect | type | NamedIndividual |
| The_Aquatic_Effect | label | "The Aquatic Effect" |

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
