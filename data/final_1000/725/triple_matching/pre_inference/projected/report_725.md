# Triple matching report: 725

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jacques_Jaccard | hasDeathPlace | Los_Angeles_California |
| Riders_of_the_Plains | hasDirector | Jacques_Jaccard |

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
| Jacques_Jaccard | type | Person |
| Jacques_Jaccard | type | NamedIndividual |
| Jacques_Jaccard | label | "Jacques Jaccard" |
| Los_Angeles_California | type | Place |
| Los_Angeles_California | type | NamedIndividual |
| Los_Angeles_California | label | "Los Angeles, California" |
| Riders_of_the_Plains | type | Film |
| Riders_of_the_Plains | type | NamedIndividual |
| Riders_of_the_Plains | label | "Riders of the Plains" |

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
