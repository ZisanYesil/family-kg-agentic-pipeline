# Triple matching report: 227

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_Man_in_Grey | hasPublicationDate | "1943"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Queen_s_Traitor | hasPublicationDate | "1967"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| The_Man_in_Grey | type | Film |
| The_Man_in_Grey | type | NamedIndividual |
| The_Man_in_Grey | label | "The Man in Grey" |
| The_Queen_s_Traitor | type | CreativeWork |
| The_Queen_s_Traitor | type | NamedIndividual |
| The_Queen_s_Traitor | label | "The Queen's Traitor" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
