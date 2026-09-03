# Triple matching report: 490

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Juan_Carlos_Gumucio | hasSpouse | Marie_Colvin |
| Marie_Colvin | hasEmployer | Sunday_Times |

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
| Juan_Carlos_Gumucio | type | Person |
| Juan_Carlos_Gumucio | type | NamedIndividual |
| Juan_Carlos_Gumucio | label | "Juan Carlos Gumucio" |
| Marie_Colvin | type | Person |
| Marie_Colvin | type | NamedIndividual |
| Marie_Colvin | label | "Marie Colvin" |
| Marie_Colvin | altLabel | "Marie Catherine Colvin" |
| Sunday_Times | type | Organization |
| Sunday_Times | type | NamedIndividual |
| Sunday_Times | label | "The Sunday Times" |

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
