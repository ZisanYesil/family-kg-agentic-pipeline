# Triple matching report: 637

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Last_White_Dishwasher | hasPublicationDate | "2008"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Year_of_Spectacular_Men | hasPublicationDate | "2017"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| The_Last_White_Dishwasher | type | Film |
| The_Last_White_Dishwasher | type | NamedIndividual |
| The_Last_White_Dishwasher | label | "The Last White Dishwasher" |
| The_Year_of_Spectacular_Men | hasPublicationDate | "2018"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Year_of_Spectacular_Men | type | Film |
| The_Year_of_Spectacular_Men | type | NamedIndividual |
| The_Year_of_Spectacular_Men | label | "The Year of Spectacular Men" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
