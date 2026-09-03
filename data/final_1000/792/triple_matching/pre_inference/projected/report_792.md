# Triple matching report: 792

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gang_Up | hasPublicationDate | "2017"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Occidentali_s_Karma | hasPublicationDate | "2017-02-10"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Gang_Up | type | CreativeWork |
| Gang_Up | type | NamedIndividual |
| Gang_Up | label | "Gang Up" |
| Gang_Up | altLabel | "Gang Up" |
| Occidentali_s_Karma | type | CreativeWork |
| Occidentali_s_Karma | type | NamedIndividual |
| Occidentali_s_Karma | label | "Occidentali's Karma" |
| Occidentali_s_Karma | altLabel | "Occidentali's Karma" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
