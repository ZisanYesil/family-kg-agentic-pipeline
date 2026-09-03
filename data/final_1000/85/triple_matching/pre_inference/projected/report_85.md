# Triple matching report: 85

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alexandre_Berthier_3rd_Prince_of_Wagram | hasParent | Napoléon_Alexandre_Berthier |
| Napoléon_Alexandre_Berthier | hasParent | Duchess_Maria_Elisabeth_in_Bavaria |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Alexandre_Berthier_3rd_Prince_of_Wagram | type | Person |
| Alexandre_Berthier_3rd_Prince_of_Wagram | type | NamedIndividual |
| Alexandre_Berthier_3rd_Prince_of_Wagram | label | "Alexandre Berthier, 3rd Prince of Wagram" |
| Alexandre_Berthier_3rd_Prince_of_Wagram | altLabel | "Louis Philippe Marie \"Alexandre\" Berthier" |
| Duchess_Maria_Elisabeth_in_Bavaria | type | Person |
| Duchess_Maria_Elisabeth_in_Bavaria | type | NamedIndividual |
| Duchess_Maria_Elisabeth_in_Bavaria | label | "Duchess Maria Elisabeth in Bavaria" |
| Napoléon_Alexandre_Berthier | type | Person |
| Napoléon_Alexandre_Berthier | type | NamedIndividual |
| Napoléon_Alexandre_Berthier | label | "Napoléon Alexandre Berthier" |
| Napoléon_Alexandre_Berthier | altLabel | "Napoléon Alexandre Louis Joseph Berthier" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
