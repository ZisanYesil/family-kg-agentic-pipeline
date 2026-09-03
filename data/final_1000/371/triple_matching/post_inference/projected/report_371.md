# Triple matching report: 371

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Agrippina_the_Elder | type | Agent |
| Agrippina_the_Elder | type | Person |
| Julia_Drusilla | type | Agent |
| Julia_Drusilla | type | Person |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Agrippina_the_Elder | hasChild | Gaius |
| Gaius | hasChild | Julia_Drusilla |
| Gaius | hasParent | Agrippina_the_Elder |
| Gaius | type | Agent |
| Gaius | type | Person |
| Julia_Drusilla | hasParent | Gaius |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Agrippina_the_Elder | hasChild | caligula |
| Julia_Drusilla | hasParent | caligula |
| caligula | hasChild | Julia_Drusilla |
| caligula | hasParent | Agrippina_the_Elder |
| caligula | type | Agent |
| caligula | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.400000 |
| Recall | 0.400000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
