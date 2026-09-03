# Triple matching report: 565

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Eduard_Künneke | hasChild | Evelyn_Künneke |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Cousin_from_Nowhere | hasComposer | Eduard_Künneke |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Eduard_Künneke | hasBirthDate | "1885-01-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Eduard_Künneke | hasDeathDate | "1953-10-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Eduard_Künneke | type | Person |
| Eduard_Künneke | type | NamedIndividual |
| Eduard_Künneke | label | "Eduard Künneke" |
| Evelyn_Künneke | type | Person |
| Evelyn_Künneke | type | NamedIndividual |
| Evelyn_Künneke | label | "Evelyn Künneke" |
| The_Cousin_from_Nowhere | type | Film |
| The_Cousin_from_Nowhere | type | NamedIndividual |
| The_Cousin_from_Nowhere | label | "The Cousin From Nowhere (1953 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
