# Triple matching report: 460

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Jean_Armand_Charlemagne | hasBirthDate | "1753-11-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_Armand_Charlemagne | hasDeathDate | "1838-03-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Ashburnham_2nd_Earl_of_Ashburnham | hasBirthDate | "1724-10-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Ashburnham_2nd_Earl_of_Ashburnham | hasDeathDate | "1812-04-08"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Jean_Armand_Charlemagne | type | Person |
| Jean_Armand_Charlemagne | type | NamedIndividual |
| Jean_Armand_Charlemagne | label | "Jean Armand Charlemagne" |
| John_Ashburnham_2nd_Earl_of_Ashburnham | type | Person |
| John_Ashburnham_2nd_Earl_of_Ashburnham | type | NamedIndividual |
| John_Ashburnham_2nd_Earl_of_Ashburnham | label | "John Ashburnham, 2nd Earl of Ashburnham" |

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
