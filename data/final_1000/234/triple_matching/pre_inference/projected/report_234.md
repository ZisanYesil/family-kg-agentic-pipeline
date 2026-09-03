# Triple matching report: 234

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
| Murray_s_Magazine | hasInception | "1887"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Progetto_Babele | hasInception | "2002"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| murrays_magazine | hasPublicationDate | "1887"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| murrays_magazine | type | CreativeWork |
| murrays_magazine | type | NamedIndividual |
| murrays_magazine | label | "Murray's Magazine" |
| progetto_babele | hasPublicationDate | "2002"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| progetto_babele | type | CreativeWork |
| progetto_babele | type | NamedIndividual |
| progetto_babele | label | "Progetto Babele" |

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
