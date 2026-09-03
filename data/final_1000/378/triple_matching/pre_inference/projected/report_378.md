# Triple matching report: 378

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Adolphe_Berty | hasBirthDate | "1818-05-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Adolphe_Berty | hasDeathDate | "1867-08-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hamlet_Gonashvili | hasBirthDate | "1928-06-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hamlet_Gonashvili | hasDeathDate | "1985-07-25"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Adolphe_Berty | type | Person |
| Adolphe_Berty | type | NamedIndividual |
| Adolphe_Berty | label | "Adolphe Berty" |
| Adolphe_Berty | altLabel | "Boulet" |
| Hamlet_Gonashvili | type | Person |
| Hamlet_Gonashvili | type | NamedIndividual |
| Hamlet_Gonashvili | label | "Hamlet Gonashvili" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
