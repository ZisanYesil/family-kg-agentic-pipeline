# Triple matching report: 856

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Arshad_Khan | hasCountry | Pakistan |
| Arshad_Khan | type | Agent |
| Arshad_Khan | type | Person |
| Daadagiri | hasCreator | Arshad_Khan |
| Daadagiri | hasDirector | Arshad_Khan |
| Daadagiri | type | Artifact |
| Daadagiri | type | CreativeWork |
| Daadagiri | type | Film |
| Pakistan | type | Country |
| Pakistan | type | Place |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Arshad_Khan | hasCountry | country_australia |
| country_australia | type | Country |
| country_australia | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 13 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.769231 |
| Recall | 1.000000 |
| F1 score | 0.869565 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
