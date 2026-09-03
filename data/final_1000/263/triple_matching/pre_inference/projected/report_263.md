# Triple matching report: 263

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Karel_Lamač | hasDeathPlace | Hamburg_Germany |
| The_Lantern | hasDirector | Karel_Lamač |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Hamburg_Germany | type | Place |
| Hamburg_Germany | type | NamedIndividual |
| Hamburg_Germany | label | "Hamburg, Germany" |
| Hamburg_Germany | altLabel | "Hamburg" |
| Hamburg_Germany | altLabel | "Hamburg, Germany" |
| Karel_Lamač | type | Person |
| Karel_Lamač | type | NamedIndividual |
| Karel_Lamač | label | "Karel Lamač" |
| Karel_Lamač | altLabel | "Karel Lamač" |
| The_Lantern | type | Film |
| The_Lantern | type | NamedIndividual |
| The_Lantern | label | "The Lantern" |
| The_Lantern | altLabel | "The Lantern" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
