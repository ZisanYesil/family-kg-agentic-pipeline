# Triple matching report: 144

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Haughton | hasCountry | Canadian |
| J_Hervé_Proulx | hasCountry | Canadian |

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
| Canadian | type | Country |
| Canadian | type | NamedIndividual |
| Canadian | label | "Canada" |
| Canadian | altLabel | "Canadian" |
| Chris_Haughton | type | Person |
| Chris_Haughton | type | NamedIndividual |
| Chris_Haughton | label | "Chris Haughton" |
| J_Hervé_Proulx | type | Person |
| J_Hervé_Proulx | type | NamedIndividual |
| J_Hervé_Proulx | label | "J. Hervé Proulx" |

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
