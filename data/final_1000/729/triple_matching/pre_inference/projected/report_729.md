# Triple matching report: 729

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Au_revoir_les_enfants | hasPublicationDate | "1987"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Physical_Jerks | hasPublicationDate | "1997"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Au_revoir_les_enfants | type | Film |
| Au_revoir_les_enfants | type | NamedIndividual |
| Au_revoir_les_enfants | label | "Au revoir les enfants" |
| Au_revoir_les_enfants | altLabel | "Au Revoir Les Enfants" |
| Physical_Jerks | type | Film |
| Physical_Jerks | type | NamedIndividual |
| Physical_Jerks | label | "Physical Jerks" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
