# Triple matching report: 62

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Leni_Riefenstahl | hasBurialPlace | Munich_Waldfriedhof |
| Tag_der_Freiheit_Unsere_Wehrmacht | hasDirector | Leni_Riefenstahl |

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
| Leni_Riefenstahl | type | Person |
| Leni_Riefenstahl | type | NamedIndividual |
| Leni_Riefenstahl | label | "Leni Riefenstahl" |
| Leni_Riefenstahl | altLabel | "Helene Bertha Amalie \"Leni\" Riefenstahl" |
| Munich_Waldfriedhof | type | Place |
| Munich_Waldfriedhof | type | NamedIndividual |
| Munich_Waldfriedhof | label | "Munich Waldfriedhof" |
| Tag_der_Freiheit_Unsere_Wehrmacht | type | Film |
| Tag_der_Freiheit_Unsere_Wehrmacht | type | NamedIndividual |
| Tag_der_Freiheit_Unsere_Wehrmacht | label | "Tag der Freiheit: Unsere Wehrmacht" |

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
