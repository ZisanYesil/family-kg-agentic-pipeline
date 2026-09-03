# Triple matching report: 352

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Johann_Adolf_of_Saxe_Gotha_Altenburg | hasBirthDate | "1721-05-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Johann_Adolf_of_Saxe_Gotha_Altenburg | hasDeathDate | "1799-04-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jules_Brunet | hasBirthDate | "1838-01-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jules_Brunet | hasDeathDate | "1911-08-12"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Johann_Adolf_of_Saxe_Gotha_Altenburg | type | Person |
| Johann_Adolf_of_Saxe_Gotha_Altenburg | type | NamedIndividual |
| Johann_Adolf_of_Saxe_Gotha_Altenburg | label | "Johann Adolf of Saxe-Gotha-Altenburg" |
| Jules_Brunet | type | Person |
| Jules_Brunet | type | NamedIndividual |
| Jules_Brunet | label | "Jules Brunet" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
