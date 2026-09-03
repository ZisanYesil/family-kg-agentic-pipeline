# Triple matching report: 783

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gianni_Versace | hasDeathPlace | Miami_Beach |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Versus | hasFounder | Gianni_Versace |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Gianni_Versace | type | Person |
| Gianni_Versace | type | NamedIndividual |
| Gianni_Versace | label | "Gianni Versace" |
| Gianni_Versace | altLabel | "Giovanni Maria Versace" |
| Miami_Beach | type | Place |
| Miami_Beach | type | NamedIndividual |
| Miami_Beach | label | "Casa Casuarina" |
| Miami_Beach | altLabel | "Miami Beach mansion Casa Casuarina" |
| versus_versace_artifact | type | Artifact |
| versus_versace_artifact | type | NamedIndividual |
| versus_versace_artifact | label | "Versus (Versace)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
