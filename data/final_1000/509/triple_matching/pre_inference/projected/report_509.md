# Triple matching report: 509

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Orlando_Dauphin_of_France | hasParent | Charles_VIII_of_France |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charles_VIII_of_France | hasCauseOfDeath | stroke |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Orlando_Dauphin_of_France | type | Person |
| Charles_Orlando_Dauphin_of_France | type | NamedIndividual |
| Charles_Orlando_Dauphin_of_France | label | "Charles Orlando, Dauphin of France" |
| Charles_VIII_of_France | hasCauseOfDeath | accidental_head_injury |
| Charles_VIII_of_France | type | Person |
| Charles_VIII_of_France | type | NamedIndividual |
| Charles_VIII_of_France | label | "Charles VIII of France" |
| accidental_head_injury | type | CauseOfDeath |
| accidental_head_injury | type | NamedIndividual |
| accidental_head_injury | label | "accidental head injury (struck head on door lintel)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
