# Triple matching report: 81

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Saint_Ignatius_College_Adelaide | hasCountry | Australia |
| St_Joseph_s_College_Gregory_Terrace | hasCountry | Australia |

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
| Australia | type | Country |
| Australia | type | NamedIndividual |
| Australia | label | "Australia" |
| Saint_Ignatius_College_Adelaide | type | EducationalInstitution |
| Saint_Ignatius_College_Adelaide | type | NamedIndividual |
| Saint_Ignatius_College_Adelaide | label | "Saint Ignatius' College, Adelaide" |
| St_Joseph_s_College_Gregory_Terrace | type | EducationalInstitution |
| St_Joseph_s_College_Gregory_Terrace | type | NamedIndividual |
| St_Joseph_s_College_Gregory_Terrace | label | "St Joseph's College, Gregory Terrace" |

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
