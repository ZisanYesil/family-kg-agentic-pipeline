# Triple matching report: 768

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Balls_Out | hasDirector | Andrew_Disney |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Andrew_Disney | hasEducatedAt | Tisch |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Andrew_Disney | hasEducatedAt | edu_tisch_school_of_the_arts |
| Andrew_Disney | type | Person |
| Andrew_Disney | type | NamedIndividual |
| Andrew_Disney | label | "Andrew Disney" |
| Balls_Out | type | Film |
| Balls_Out | type | NamedIndividual |
| Balls_Out | label | "Balls Out (2014 film)" |
| edu_tisch_school_of_the_arts | type | EducationalInstitution |
| edu_tisch_school_of_the_arts | type | NamedIndividual |
| edu_tisch_school_of_the_arts | label | "Tisch School of the Arts" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
