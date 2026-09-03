# Triple matching report: 43

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Polish_Russian_War | hasDirector | Xawery_Żuławski |
| Xawery_Żuławski | hasEducatedAt | National_Film_School_in_Łódź |

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
| National_Film_School_in_Łódź | type | EducationalInstitution |
| National_Film_School_in_Łódź | type | NamedIndividual |
| National_Film_School_in_Łódź | label | "National Film School in Łódź" |
| Polish_Russian_War | type | Film |
| Polish_Russian_War | type | NamedIndividual |
| Polish_Russian_War | label | "Polish-Russian War" |
| Xawery_Żuławski | type | Person |
| Xawery_Żuławski | type | NamedIndividual |
| Xawery_Żuławski | label | "Xawery Żuławski" |

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
