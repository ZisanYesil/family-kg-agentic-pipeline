# Triple matching report: 719

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Cupid_the_Cowpuncher | hasCountry | American |
| Hashimura_Togo | hasCountry | American |

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
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Cupid_the_Cowpuncher | type | Film |
| Cupid_the_Cowpuncher | type | NamedIndividual |
| Cupid_the_Cowpuncher | label | "Cupid the Cowpuncher" |
| Hashimura_Togo | type | Film |
| Hashimura_Togo | type | NamedIndividual |
| Hashimura_Togo | label | "Hashimura Togo" |

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
