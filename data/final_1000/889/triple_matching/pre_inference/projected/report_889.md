# Triple matching report: 889

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Duccio_Tessari | hasDeathDate | "1994-09-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Edwin_L_Marin | hasDeathDate | "1951-05-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Henry_Goes_Arizona | hasDirector | Edwin_L_Marin |
| Tex_and_the_Lord_of_the_Deep | hasDirector | Duccio_Tessari |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Duccio_Tessari | type | Person |
| Duccio_Tessari | type | NamedIndividual |
| Duccio_Tessari | label | "Duccio Tessari" |
| Edwin_L_Marin | type | Person |
| Edwin_L_Marin | type | NamedIndividual |
| Edwin_L_Marin | label | "Edwin L. Marin" |
| Henry_Goes_Arizona | type | Film |
| Henry_Goes_Arizona | type | NamedIndividual |
| Henry_Goes_Arizona | label | "Henry Goes Arizona" |
| Tex_and_the_Lord_of_the_Deep | type | Film |
| Tex_and_the_Lord_of_the_Deep | type | NamedIndividual |
| Tex_and_the_Lord_of_the_Deep | label | "Tex and the Lord of the Deep" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
