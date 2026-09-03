# Triple matching report: 771

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Stephen_Warbeck | hasBirthPlace | Southampton_Hampshire |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Billy_Elliot | hasComposer | Stephen_Warbeck |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Billy_Elliot | type | Film |
| Billy_Elliot | type | NamedIndividual |
| Billy_Elliot | label | "Billy Elliot" |
| Southampton_Hampshire | type | Place |
| Southampton_Hampshire | type | NamedIndividual |
| Southampton_Hampshire | label | "Southampton, Hampshire" |
| Stephen_Warbeck | type | Person |
| Stephen_Warbeck | type | NamedIndividual |
| Stephen_Warbeck | label | "Stephen Warbeck" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
