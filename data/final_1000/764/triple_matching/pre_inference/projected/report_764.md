# Triple matching report: 764

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Karel_Lamač | hasDeathPlace | Hamburg_Germany |
| The_Good_Soldier_Schweik | hasDirector | Karel_Lamač |

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
| Hamburg_Germany | type | Place |
| Hamburg_Germany | type | NamedIndividual |
| Hamburg_Germany | label | "Hamburg, Germany" |
| Karel_Lamač | type | Person |
| Karel_Lamač | type | NamedIndividual |
| Karel_Lamač | label | "Karel Lamač" |
| The_Good_Soldier_Schweik | type | Film |
| The_Good_Soldier_Schweik | type | NamedIndividual |
| The_Good_Soldier_Schweik | label | "The Good Soldier Schweik (1926 film)" |

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
