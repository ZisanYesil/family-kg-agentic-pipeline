# Triple matching report: 637

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| The_Last_White_Dishwasher | hasPublicationDate | "2008"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Last_White_Dishwasher | type | Artifact |
| The_Last_White_Dishwasher | type | CreativeWork |
| The_Year_of_Spectacular_Men | type | Artifact |
| The_Year_of_Spectacular_Men | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Year_of_Spectacular_Men | hasPublicationDate | "2017"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| The_Last_White_Dishwasher | type | Film |
| The_Year_of_Spectacular_Men | hasPublicationDate | "2018"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Year_of_Spectacular_Men | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 9 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.625000 |
| Recall | 0.833333 |
| F1 score | 0.714286 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
