# Triple matching report: 811

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Agrippina_the_Elder | hasCauseOfDeath | starvation |
| Agrippina_the_Younger | hasParent | Agrippina_the_Elder |

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
| Agrippina_the_Elder | type | Person |
| Agrippina_the_Elder | type | NamedIndividual |
| Agrippina_the_Elder | label | "Agrippina the Elder" |
| Agrippina_the_Younger | type | Person |
| Agrippina_the_Younger | type | NamedIndividual |
| Agrippina_the_Younger | label | "Agrippina the Younger" |
| starvation | type | CauseOfDeath |
| starvation | type | NamedIndividual |
| starvation | label | "starvation" |

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
