# Triple matching report: 856

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Arshad_Khan | hasCountry | Pakistan |
| Daadagiri | hasDirector | Arshad_Khan |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Arshad_Khan | hasCountry | country_australia |
| Arshad_Khan | type | Person |
| Arshad_Khan | type | NamedIndividual |
| Arshad_Khan | label | "Arshad Khan" |
| Daadagiri | type | Film |
| Daadagiri | type | NamedIndividual |
| Daadagiri | label | "Daadagiri" |
| Pakistan | type | Country |
| Pakistan | type | NamedIndividual |
| Pakistan | label | "Pakistan" |
| Pakistan | altLabel | "Pakistani" |
| country_australia | type | Country |
| country_australia | type | NamedIndividual |
| country_australia | label | "Australia" |
| country_australia | altLabel | "Australian" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.117647 |
| Recall | 1.000000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
