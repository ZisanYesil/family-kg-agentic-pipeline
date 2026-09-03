# Triple matching report: 569

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| L_Assiette_au_Beurre | hasInception | "1901"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Pnai_Plus | hasInception | "1989"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| lassiette_au_beurre | hasPublicationDate | "1901"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| lassiette_au_beurre | type | CreativeWork |
| lassiette_au_beurre | type | NamedIndividual |
| lassiette_au_beurre | label | "L'Assiette Au Beurre" |
| pnai_plus | hasPublicationDate | "1989"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| pnai_plus | type | CreativeWork |
| pnai_plus | type | NamedIndividual |
| pnai_plus | label | "Pnai Plus" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 0 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
