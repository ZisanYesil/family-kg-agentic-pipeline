# Triple matching report: 457

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jean_Tschumi | hasEmployer | École_polytechnique_fédérale_de_Lausanne |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bernard_Tschumi | hasParent | Jean_Tschumi |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Bernard_Tschumi | type | Person |
| Bernard_Tschumi | type | NamedIndividual |
| Bernard_Tschumi | label | "Bernard Tschumi" |
| Jean_Tschumi | hasChild | Bernard_Tschumi |
| Jean_Tschumi | type | Person |
| Jean_Tschumi | type | NamedIndividual |
| Jean_Tschumi | label | "Jean Tschumi" |
| École_polytechnique_fédérale_de_Lausanne | type | Organization |
| École_polytechnique_fédérale_de_Lausanne | type | NamedIndividual |
| École_polytechnique_fédérale_de_Lausanne | label | "École Polytechnique Fédérale de Lausanne" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
