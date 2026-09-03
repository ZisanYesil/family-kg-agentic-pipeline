# Triple matching report: 321

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bamba_Müller | hasDeathDate | "1887-09-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Princess_Sophia_Alexandrovna_Duleep_Singh | hasParent | Bamba_Müller |

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
| Bamba_Müller | type | Person |
| Bamba_Müller | type | NamedIndividual |
| Bamba_Müller | label | "Bamba Müller" |
| Bamba_Müller | altLabel | "Bamba Müller" |
| Bamba_Müller | altLabel | "Lady Duleep Singh" |
| Bamba_Müller | altLabel | "Maharani Bamba" |
| Princess_Sophia_Alexandrovna_Duleep_Singh | type | Person |
| Princess_Sophia_Alexandrovna_Duleep_Singh | type | NamedIndividual |
| Princess_Sophia_Alexandrovna_Duleep_Singh | label | "Sophia Duleep Singh" |
| Princess_Sophia_Alexandrovna_Duleep_Singh | altLabel | "Princess Sophia Alexandrovna Duleep Singh" |
| Princess_Sophia_Alexandrovna_Duleep_Singh | altLabel | "Sophia Duleep Singh" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
