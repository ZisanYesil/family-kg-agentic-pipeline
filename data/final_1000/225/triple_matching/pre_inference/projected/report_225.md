# Triple matching report: 225

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Sarah_Frances_Elizabeth_Chatto | hasParent | Princess_Margaret |
| Princess_Margaret | hasCauseOfDeath | stroke |

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
| Lady_Sarah_Frances_Elizabeth_Chatto | type | Person |
| Lady_Sarah_Frances_Elizabeth_Chatto | type | NamedIndividual |
| Lady_Sarah_Frances_Elizabeth_Chatto | label | "Lady Sarah Chatto" |
| Princess_Margaret | type | Person |
| Princess_Margaret | type | NamedIndividual |
| Princess_Margaret | label | "Princess Margaret, Countess of Snowdon" |
| stroke | type | CauseOfDeath |
| stroke | type | NamedIndividual |
| stroke | label | "stroke" |

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
