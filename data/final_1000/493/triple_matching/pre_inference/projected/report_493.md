# Triple matching report: 493

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Song_to_the_Siren | hasPerformer | Tim_Buckley |
| Tim_Buckley | hasCauseOfDeath | overdose |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Song_to_the_Siren | type | MusicalWork |
| Song_to_the_Siren | type | NamedIndividual |
| Song_to_the_Siren | label | "Song to the Siren" |
| Tim_Buckley | type | Person |
| Tim_Buckley | type | NamedIndividual |
| Tim_Buckley | label | "Tim Buckley" |
| Tim_Buckley | altLabel | "Timothy Charles Buckley III" |
| overdose | type | CauseOfDeath |
| overdose | type | NamedIndividual |
| overdose | label | "heroin overdose" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
