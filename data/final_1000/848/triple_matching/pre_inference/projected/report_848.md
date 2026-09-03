# Triple matching report: 848

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Tracy | hasSpouse | Spencer_Tracy |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Spencer_Tracy | hasEducatedAt | American_Academy_of_Dramatic_Arts |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Tracy | type | Person |
| Louise_Tracy | type | NamedIndividual |
| Louise_Tracy | label | "Louise Tracy" |
| Spencer_Tracy | hasEducatedAt | ripon_college |
| Spencer_Tracy | type | Person |
| Spencer_Tracy | type | NamedIndividual |
| Spencer_Tracy | label | "Spencer Tracy" |
| ripon_college | type | EducationalInstitution |
| ripon_college | type | NamedIndividual |
| ripon_college | label | "Ripon College" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
