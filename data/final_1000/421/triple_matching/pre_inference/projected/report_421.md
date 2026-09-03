# Triple matching report: 421

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gwendolyn_Graham | hasParent | Bob_Graham |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bob_Graham | hasEmployer | Harvard |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Bob_Graham | hasEmployer | bob_graham_center |
| Bob_Graham | type | Person |
| Bob_Graham | type | NamedIndividual |
| Bob_Graham | label | "Bob Graham" |
| Gwendolyn_Graham | type | Person |
| Gwendolyn_Graham | type | NamedIndividual |
| Gwendolyn_Graham | label | "Gwendolyn Graham" |
| Gwendolyn_Graham | altLabel | "Gwen Graham" |
| bob_graham_center | type | Organization |
| bob_graham_center | type | NamedIndividual |
| bob_graham_center | label | "Bob Graham Center for Public Service" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
