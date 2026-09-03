# Triple matching report: 497

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Alex_P | hasCountry | Sweden |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Replay | hasComposer | Alex_P |

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Alex_P | hasCountry | greece |
| Alex_P | type | Person |
| Alex_P | type | NamedIndividual |
| Alex_P | label | "Alex P" |
| Alex_P | altLabel | "Alexander \"Alex P\" Papaconstantinou" |
| Replay | hasCreator | Alex_P |
| Replay | type | MusicalWork |
| Replay | type | NamedIndividual |
| Replay | label | "Replay" |
| Sweden | type | Country |
| Sweden | type | NamedIndividual |
| Sweden | label | "Sweden" |
| Sweden | altLabel | "Swedish" |
| greece | type | Country |
| greece | type | NamedIndividual |
| greece | label | "Greece" |
| greece | altLabel | "Greek" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 19 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.055556 |
| Recall | 0.500000 |
| F1 score | 0.100000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
