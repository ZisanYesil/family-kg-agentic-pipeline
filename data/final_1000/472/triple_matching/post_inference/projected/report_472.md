# Triple matching report: 472

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Picturegoer | hasInception | "1911"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Picturegoer | type | Agent |
| Picturegoer | type | Organization |
| Scribner_s_Monthly | hasInception | "1870"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Scribner_s_Monthly | type | Agent |
| Scribner_s_Monthly | type | Organization |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| picturegoer_1911 | hasPublicationDate | "1911"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| picturegoer_1911 | type | Artifact |
| picturegoer_1911 | type | CreativeWork |
| scribners_monthly_1870 | hasPublicationDate | "1870"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| scribners_monthly_1870 | type | Artifact |
| scribners_monthly_1870 | type | CreativeWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 0 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 12 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
