# Triple matching report: 93

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jack_Robertson_footballer_born_1902 | hasCountry | Australian |
| Peter_Levy_cinematographer | hasCountry | Australian |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Australian | type | Country |
| Australian | type | NamedIndividual |
| Australian | label | "Australia" |
| Australian | altLabel | "Australian" |
| Jack_Robertson_footballer_born_1902 | type | Person |
| Jack_Robertson_footballer_born_1902 | type | NamedIndividual |
| Jack_Robertson_footballer_born_1902 | label | "Jack Robertson" |
| Jack_Robertson_footballer_born_1902 | altLabel | "Jack Robertson (footballer, born 1902)" |
| Peter_Levy_cinematographer | type | Person |
| Peter_Levy_cinematographer | type | NamedIndividual |
| Peter_Levy_cinematographer | label | "Peter Levy" |
| Peter_Levy_cinematographer | altLabel | "Peter Levy (cinematographer)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
