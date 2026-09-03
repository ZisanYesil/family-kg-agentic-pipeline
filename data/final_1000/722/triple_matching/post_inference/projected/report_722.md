# Triple matching report: 722

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Australian | type | Country |
| Australian | type | Place |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| King_Gizzard_the_Lizard_Wizard | hasCountry | Australian |
| King_Gizzard_the_Lizard_Wizard | type | Artifact |
| Rebecca_s_Empire | hasCountry | Australian |
| Rebecca_s_Empire | type | Artifact |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| king_gizzard_lizard_wizard | hasCountry | Australian |
| king_gizzard_lizard_wizard | type | Agent |
| king_gizzard_lizard_wizard | type | Organization |
| rebeccas_empire | hasCountry | Australian |
| rebeccas_empire | type | Agent |
| rebeccas_empire | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.250000 |
| Recall | 0.333333 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
