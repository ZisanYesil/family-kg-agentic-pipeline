# Triple matching report: 248

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| George_McCowan | hasCauseOfDeath | emphysema |
| Starsky_and_Hutch_on_Playboy_Island | hasDirector | George_McCowan |

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
| George_McCowan | type | Person |
| George_McCowan | type | NamedIndividual |
| George_McCowan | label | "George McCowan" |
| Starsky_and_Hutch_on_Playboy_Island | type | Film |
| Starsky_and_Hutch_on_Playboy_Island | type | NamedIndividual |
| Starsky_and_Hutch_on_Playboy_Island | label | "Starsky and Hutch on Playboy Island" |
| emphysema | type | CauseOfDeath |
| emphysema | type | NamedIndividual |
| emphysema | label | "emphysema" |

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
