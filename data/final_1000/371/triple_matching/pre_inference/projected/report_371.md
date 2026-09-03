# Triple matching report: 371

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gaius | hasParent | Agrippina_the_Elder |
| Julia_Drusilla | hasParent | Gaius |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Agrippina_the_Elder | type | Person |
| Agrippina_the_Elder | type | NamedIndividual |
| Agrippina_the_Elder | label | "Agrippina the Elder" |
| Julia_Drusilla | hasParent | caligula |
| Julia_Drusilla | type | Person |
| Julia_Drusilla | type | NamedIndividual |
| Julia_Drusilla | label | "Julia Drusilla" |
| caligula | hasParent | Agrippina_the_Elder |
| caligula | type | Person |
| caligula | type | NamedIndividual |
| caligula | label | "Caligula" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
