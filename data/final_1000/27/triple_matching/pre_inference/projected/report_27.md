# Triple matching report: 27

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Catherine_Allégret | hasParent | Yves_Allégret |
| Yves_Allégret | hasSibling | Marc_Allégret |

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
| Catherine_Allégret | type | Person |
| Catherine_Allégret | type | NamedIndividual |
| Catherine_Allégret | label | "Catherine Allégret" |
| Marc_Allégret | type | Person |
| Marc_Allégret | type | NamedIndividual |
| Marc_Allégret | label | "Marc Allégret" |
| Yves_Allégret | type | Person |
| Yves_Allégret | type | NamedIndividual |
| Yves_Allégret | label | "Yves Allégret" |

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
