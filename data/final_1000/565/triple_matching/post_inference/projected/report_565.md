# Triple matching report: 565

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Eduard_Künneke | hasChild | Evelyn_Künneke |
| Eduard_Künneke | type | Agent |
| Eduard_Künneke | type | Person |
| Evelyn_Künneke | hasParent | Eduard_Künneke |
| Evelyn_Künneke | type | Agent |
| Evelyn_Künneke | type | Person |
| The_Cousin_from_Nowhere | hasComposer | Eduard_Künneke |
| The_Cousin_from_Nowhere | hasCreator | Eduard_Künneke |
| The_Cousin_from_Nowhere | type | Artifact |
| The_Cousin_from_Nowhere | type | CreativeWork |

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
| Eduard_Künneke | hasBirthDate | "1885-01-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Eduard_Künneke | hasDeathDate | "1953-10-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Cousin_from_Nowhere | type | Film |

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
