# Triple matching report: 179

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Johann_Georg_Tralles | hasBirthDate | "1763-10-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Johann_Georg_Tralles | hasDeathDate | "1822-11-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Raymond_Adolphe_Séré_de_Rivières | hasBirthDate | "1815-05-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Raymond_Adolphe_Séré_de_Rivières | hasDeathDate | "1895-02-16"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Johann_Georg_Tralles | type | Person |
| Johann_Georg_Tralles | type | NamedIndividual |
| Johann_Georg_Tralles | label | "Johann Georg Tralles" |
| Johann_Georg_Tralles | altLabel | "Johann Georg Tralles" |
| Raymond_Adolphe_Séré_de_Rivières | type | Person |
| Raymond_Adolphe_Séré_de_Rivières | type | NamedIndividual |
| Raymond_Adolphe_Séré_de_Rivières | label | "Raymond Adolphe Séré de Rivières" |
| Raymond_Adolphe_Séré_de_Rivières | altLabel | "Raymond Adolphe Séré de Rivières" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.333333 |
| Recall | 1.000000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
