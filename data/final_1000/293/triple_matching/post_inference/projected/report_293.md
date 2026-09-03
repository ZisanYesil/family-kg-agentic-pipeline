# Triple matching report: 293

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Beauty_and_the_Bastard | hasPublicationDate | "2005"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Beauty_and_the_Bastard | type | Artifact |
| Beauty_and_the_Bastard | type | CreativeWork |
| Crazy_on_the_Outside | hasPublicationDate | "2010"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Crazy_on_the_Outside | type | Artifact |
| Crazy_on_the_Outside | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Beauty_and_the_Bastard | type | Film |
| Crazy_on_the_Outside | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
