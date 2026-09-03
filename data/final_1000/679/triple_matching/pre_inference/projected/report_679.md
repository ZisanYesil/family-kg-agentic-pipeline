# Triple matching report: 679

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Absalom_Baird | hasBirthDate | "1824-08-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Absalom_Baird | hasDeathDate | "1905-06-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Ashkenazi | hasBirthDate | "1915-12-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Ashkenazi | hasDeathDate | "1997-02-19"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Absalom_Baird | type | Person |
| Absalom_Baird | type | NamedIndividual |
| Absalom_Baird | label | "Absalom Baird" |
| David_Ashkenazi | type | Person |
| David_Ashkenazi | type | NamedIndividual |
| David_Ashkenazi | label | "David Vladimirovitch Ashkenazi" |
| David_Ashkenazi | altLabel | "David Ashkenazi" |

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
