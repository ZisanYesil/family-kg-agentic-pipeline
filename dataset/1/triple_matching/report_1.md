# Triple matching report: 1

# 1. Matched triples

**Count: 20**

| Subject | Predicate | Object |
|---|---|---|
| Q2083645 | hasCreator | Q530027 |
| Q2083645 | hasDirector | Q530027 |
| Q2083645 | type | Artifact |
| Q2083645 | type | CreativeWork |
| Q213 | type | Country |
| Q213 | type | Place |
| Q36704 | type | Country |
| Q36704 | type | Place |
| Q530027 | hasCitizenship | Q36704 |
| Q530027 | hasCountry | Q36704 |
| Q530027 | type | Agent |
| Q530027 | type | Person |
| Q769826 | hasCitizenship | Q213 |
| Q769826 | hasCountry | Q213 |
| Q769826 | type | Agent |
| Q769826 | type | Person |
| Q7910840 | hasCreator | Q769826 |
| Q7910840 | hasDirector | Q769826 |
| Q7910840 | type | Artifact |
| Q7910840 | type | CreativeWork |

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
| Q2083645 | hasPublicationDate | "1981"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q2083645 | type | Film |
| Q530027 | hasBirthDate | "1923-06-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q769826 | hasBirthDate | "1902-03-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q769826 | hasDeathDate | "1968-08-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q7910840 | hasPublicationDate | "1942"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q7910840 | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 27 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 27 |
| True positives (matched) | 20 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.740741 |
| Recall | 1.000000 |
| F1 score | 0.851064 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
