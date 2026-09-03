# Triple matching report: 619

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Dalida | hasDirector | Lisa_Azuelos |
| Lisa_Azuelos | hasParent | Marie_Laforêt |

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
| Dalida | type | Film |
| Dalida | type | NamedIndividual |
| Dalida | label | "Dalida (2017 film)" |
| Lisa_Azuelos | type | Person |
| Lisa_Azuelos | type | NamedIndividual |
| Lisa_Azuelos | label | "Lisa Azuelos" |
| Marie_Laforêt | type | Person |
| Marie_Laforêt | type | NamedIndividual |
| Marie_Laforêt | label | "Marie Laforêt" |

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
