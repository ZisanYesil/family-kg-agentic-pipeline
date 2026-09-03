# Triple matching report: 916

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Boaz_Davidson | hasBirthDate | "1943-11-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hospital_Massacre | hasDirector | Boaz_Davidson |
| José_María_Forqué | hasBirthDate | "1923-03-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Searching_for_Monica | hasDirector | José_María_Forqué |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Boaz_Davidson | type | Person |
| Boaz_Davidson | type | NamedIndividual |
| Boaz_Davidson | label | "Boaz Davidson" |
| Hospital_Massacre | type | Film |
| Hospital_Massacre | type | NamedIndividual |
| Hospital_Massacre | label | "Hospital Massacre" |
| José_María_Forqué | type | Person |
| José_María_Forqué | type | NamedIndividual |
| José_María_Forqué | label | "José María Forqué" |
| José_María_Forqué | altLabel | "José María Forqué Galindo" |
| Searching_for_Monica | type | Film |
| Searching_for_Monica | type | NamedIndividual |
| Searching_for_Monica | label | "Searching for Monica" |
| Searching_for_Monica | altLabel | "Buscando a Mónica" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
