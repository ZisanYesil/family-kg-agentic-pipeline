# Triple matching report: 329

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gustaf_Molander | hasBirthPlace | Helsingfors |
| One_But_a_Lion | hasDirector | Gustaf_Molander |

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
| Gustaf_Molander | type | Person |
| Gustaf_Molander | type | NamedIndividual |
| Gustaf_Molander | label | "Gustaf Molander" |
| Helsingfors | type | Place |
| Helsingfors | type | NamedIndividual |
| Helsingfors | label | "Helsingfors" |
| Helsingfors | altLabel | "Helsinki" |
| One_But_a_Lion | type | Film |
| One_But_a_Lion | type | NamedIndividual |
| One_But_a_Lion | label | "One, But a Lion!" |

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
