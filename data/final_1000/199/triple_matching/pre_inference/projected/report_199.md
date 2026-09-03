# Triple matching report: 199

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Paul_Freedman | hasEmployer | Yale |
| Sand_And_Sorrow | hasDirector | Paul_Freedman |

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
| Paul_Freedman | type | Person |
| Paul_Freedman | type | NamedIndividual |
| Paul_Freedman | label | "Paul Freedman" |
| Sand_And_Sorrow | type | Film |
| Sand_And_Sorrow | type | NamedIndividual |
| Sand_And_Sorrow | label | "Sand And Sorrow" |
| Yale | type | Organization |
| Yale | type | NamedIndividual |
| Yale | label | "Yale University" |

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
