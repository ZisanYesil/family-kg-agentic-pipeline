# Triple matching report: 973

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| For_a_Few_Extra_Dollars | hasCountry | Italian |
| Vendetta_di_zingara | hasCountry | Italian |

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
| For_a_Few_Extra_Dollars | type | Film |
| For_a_Few_Extra_Dollars | type | NamedIndividual |
| For_a_Few_Extra_Dollars | label | "For a Few Extra Dollars" |
| Italian | type | Country |
| Italian | type | NamedIndividual |
| Italian | label | "Italy" |
| Italian | altLabel | "Italian" |
| Vendetta_di_zingara | type | Film |
| Vendetta_di_zingara | type | NamedIndividual |
| Vendetta_di_zingara | label | "Vendetta di zingara" |

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
